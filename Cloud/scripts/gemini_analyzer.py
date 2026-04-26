"""
Gemini Analysis Module for Cloud Environment (Vertex AI)

This module uses Google's Gemini models via Vertex AI to analyze Reddit data,
generating insights and summaries from processed posts and comments in BigQuery.

Authentication: Uses GCP service account credentials (GOOGLE_APPLICATION_CREDENTIALS)
instead of an AI Studio API key. This bypasses AI Studio account-level quotas/blocks
and uses the GCP project's billing & quota system.

SDK: Uses the unified `google-genai` SDK (the successor to `vertexai.generative_models`,
which is deprecated and slated for removal in June 2026).

Setup requirements:
    1. Vertex AI API must be enabled on the GCP project:
       https://console.cloud.google.com/apis/library/aiplatform.googleapis.com
    2. Service account needs role: 'roles/aiplatform.user' (Vertex AI User)
    3. Billing must be enabled on the GCP project (free $300 credit works)

Owner: Sulman Khan
"""

import os
import sys
import time
from datetime import datetime
from typing import Optional

from google import genai
from google.genai import types as genai_types
from google.cloud import bigquery
from google.cloud import storage

# Add the Cloud directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUD_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(CLOUD_DIR)

from config.config import SUBREDDITS, GCS_BUCKET_NAME, GCP_CONFIG, get_gcp_credentials
from utils.custom_logging import get_logger, setup_logging

# Configure logging with absolute path
LOGS_DIR = os.path.join(CLOUD_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)
logger = setup_logging(script_name='gemini_analyzer', log_dir=LOGS_DIR)


# Constants
RESULTS_PREFIX = "results"

# Model configuration (Vertex AI)
# Vertex AI quotas are MUCH higher than AI Studio free tier and use pay-as-you-go pricing.
# For Gemini 2.5 Flash-Lite in us-central1, default quota is ~4,000 RPM (vs 15 on AI Studio).
# Pricing (per 1M tokens, Apr 2026): Flash-Lite ~$0.10 in / $0.40 out, Flash ~$0.30 in / $2.50 out.
# Estimated cost for this pipeline: <$1/month at current usage.
GEMINI_MODEL = 'gemini-2.5-flash-lite'

# Data limits - kept conservative to control token costs (not because of rate limits)
MAX_TOP_POSTS_PER_SUBREDDIT = 15  # Limit to top 15 posts per subreddit
MAX_COMMENTS_PER_POST = 10  # Limit to top 10 comments per post

# Rate limiting - Vertex AI is generous, but we stay polite. We only make ~8 requests
# per pipeline run (one per subreddit), so these limits are mostly safety nets.
MAX_DAILY_REQUESTS = 500  # Safety cap; one run = ~8 requests
MAX_REQUESTS_PER_MINUTE = 60  # Vertex AI default is much higher, but stay polite
REQUEST_DELAY_SECONDS = 1  # Brief delay between requests

# Request tracking
request_count = 0
last_request_time = None


def upload_to_gcs(local_file_path: str, gcs_blob_path: str, storage_client: storage.Client):
    """
    Upload a file to Google Cloud Storage.
    
    Args:
        local_file_path (str): Path to the local file
        gcs_blob_path (str): Path in GCS where the file should be uploaded
        storage_client (storage.Client): GCS client instance
    """
    try:
        bucket = storage_client.bucket(GCS_BUCKET_NAME)
        blob = bucket.blob(gcs_blob_path)
        
        blob.upload_from_filename(local_file_path)
        logger.info(f"Successfully uploaded {local_file_path} to gs://{GCS_BUCKET_NAME}/{gcs_blob_path}")
    except Exception as e:
        logger.error(f"Error uploading to GCS: {str(e)}")
        raise

def get_gcs_path(year: str, month: str, day: str, filename: str) -> str:
    """
    Construct the GCS path for a file following the specified directory structure.
    
    Args:
        year (str): Year component of the path
        month (str): Month component of the path
        day (str): Day component of the path
        filename (str): Name of the file
        
    Returns:
        str: Full GCS path
    """
    return f"{RESULTS_PREFIX}/{year}/{month}/{day}/{filename}"

def check_and_wait_for_quota():
    """
    Enforce rate limiting by tracking requests and adding delays.
    Implements both per-minute and per-day quota checks.
    
    Returns:
        bool: True if request can proceed, False if daily quota exceeded
    """
    global request_count, last_request_time
    
    # Check daily quota
    if request_count >= MAX_DAILY_REQUESTS:
        logger.error(f"Daily quota of {MAX_DAILY_REQUESTS} requests reached. Stopping to avoid hitting API limits.")
        return False
    
    # Enforce delay between requests to stay under RPM limit
    if last_request_time is not None:
        time_since_last_request = time.time() - last_request_time
        if time_since_last_request < REQUEST_DELAY_SECONDS:
            sleep_time = REQUEST_DELAY_SECONDS - time_since_last_request
            logger.info(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
    
    return True

def make_gemini_request_with_retry(
    genai_client: genai.Client,
    prompt: str,
    max_retries: int = 3,
) -> genai_types.GenerateContentResponse:
    """
    Make a Gemini API request with exponential backoff for rate limit errors.

    Args:
        genai_client: The google-genai Client instance (configured for Vertex AI)
        prompt: The prompt to send
        max_retries: Maximum number of retry attempts

    Returns:
        The GenerateContentResponse from Vertex AI

    Raises:
        Exception: If all retries are exhausted
    """
    global request_count, last_request_time

    for attempt in range(max_retries):
        try:
            if not check_and_wait_for_quota():
                raise Exception("Daily quota exceeded")

            response = genai_client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            request_count += 1
            last_request_time = time.time()
            logger.info(f"Request successful. Total requests today: {request_count}/{MAX_DAILY_REQUESTS}")

            return response
            
        except Exception as e:
            error_str = str(e)

            # Unrecoverable Vertex AI errors - retrying won't help. Common causes:
            #   - Vertex AI API not enabled on the project
            #   - Service account missing 'roles/aiplatform.user'
            #   - Billing not enabled on the project
            #   - Model not available in the selected region
            unrecoverable_errors = [
                "PERMISSION_DENIED",
                "permission denied",
                "billing",
                "has not been used",  # API not enabled
                "is not enabled",
                "NOT_FOUND",  # model not available in region
                "INVALID_ARGUMENT",
            ]
            if any(err.lower() in error_str.lower() for err in unrecoverable_errors):
                logger.error(f"Unrecoverable Vertex AI error - retrying won't help: {error_str}")
                logger.error(
                    "Check: (1) Vertex AI API enabled, (2) service account has "
                    "'roles/aiplatform.user', (3) billing enabled on project "
                    f"'{GCP_CONFIG.get('project_id')}', (4) model available in region "
                    f"'{GCP_CONFIG.get('region')}'"
                )
                raise

            # Rate limit / quota error - worth retrying with backoff
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str or "quota" in error_str.lower():
                if attempt < max_retries - 1:
                    wait_time = 30 * (2 ** attempt)
                    logger.warning(f"Rate limit hit. Waiting {wait_time}s before retry {attempt + 1}/{max_retries}")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Max retries exhausted. Rate limit error: {error_str}")
                    raise
            else:
                logger.error(f"Non-rate-limit error: {error_str}")
                raise

    raise Exception("Failed to make request after all retries")

def create_prompt_template():
    """Return the standard prompt template for Gemini analysis."""
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    return f"""
    Analyze the provided text files, which contain Reddit posts and comments.
    **Instructions:**
    1.  **Content Filtering:** Before any analysis, check the provided text files for the presence of harassment, hate speech, or explicit material. If such material is detected, **do not proceed with any further summarization or analysis for that particular text file. Instead, output a single line stating `Analysis Skipped: Content contains harmful material.`**
    2.   "Do not include any hate speech, harassment, or offensive language in any analysis if content does not contain harmful material."
    3.  **Ranking:** Rank the threads based on their total "Score" from highest to lowest.
    4.  **Summarization:** Utilize the provided "Summary" fields to give a brief overview of what people were discussing in each thread.
    5.  **Emotional Analysis:** Use the "Emotion Label" and "Emotion Score" to discuss the overall emotional tone of each thread. Identify any dominant emotions, and note variations.
    6.  **Point of View Extraction:** For each thread, try to extract and summarize the top 3 points of view or arguments made by different users. If there are fewer than 3 distinct viewpoints, just list what you can find.
    7.  **Links:** Embed the URL field inside of the thread titles, using Markdown.
    8.  **Output Format:** Analyze the provided text files and output in this exact format:
        ---
        title: "{{subreddit_name}} subreddit"
        date: "{current_date}"
        description: "Analysis of top discussions and trends in the {{subreddit_name}} subreddit"
        tags: ["tag1", "tag2", "tag3"]
        ---

        # Overall Ranking and Top Discussions
        *   A numbered list of the threads, ranked by their "Score", with the highest score first.
        *   Each entry should include the thread's name (with embedded link), score and a short explanation of what was discussed. Make sure the short explanation is a bullet point (it should be under each thread)
        *   Format the title with its tag and link as follows:
            * If title contains [X] tag (like [D], [R], [P], [Project], [Discussion], [Research], etc.):
                `[[X] Rest of Title](post_url)`
            * If no tag:
                `[Title](post_url)`
            Examples:
                * Title with tag: `[[D] Machine Learning Updates](https://reddit.com/...)`
                * Title with multiple tags: `[[D] [R] Machine Learning Updates](https://reddit.com/...)`
                * Title with tag at the end: `[Machine Learning Updates [D]](https://reddit.com/...)`
                * Title without tag: `[Database Performance Guide](https://reddit.com/...)`
        
        # Detailed Analysis by Thread 
        *   Each analysis should follow this format:
            **[ {{post_title}} (Score: {{Score}})](URL)**
            *  **Summary:**  {{The summary of the thread}}
            *  **Emotion:** {{The emotional tone of the thread}}
            *  **Top 3 Points of View:**
                * {{Point of view 1}}
                * {{Point of view 2}}
                * {{Point of view 3}}

    **Provided Text Files:**
    [Insert the content of your text files here, each block prefixed with "~~~" to indicate a text file]
    **Note:** If no text files are supplied, simply state: "It was very quiet in that subreddit today. Please adhere to the output format."
    """

def format_text_file(row):
    """Format a single row of data into text file format."""
    return f"""~~~
    post_id: {row.post_id}
    subreddit: {row.subreddit.lower()}
    post_score: {row.post_score}
    post_url: {row.post_url}
    comment_id: {row.comment_id}
    summary_date: {row.summary_date}
    post_content: {row.post_content}
    comment_body: {row.comment_body}
    comment_summary: {row.comment_summary}
    sentiment_score: {row.sentiment_score}
    sentiment_label: {row.sentiment_label}
    """

def get_formatted_subreddit_name(subreddit: str) -> str:
    """
    Returns a properly formatted subreddit name for display.
    
    Args:
        subreddit (str): The raw subreddit name
        
    Returns:
        str: The formatted subreddit name
    """
    subreddit_formats = {
        "claudeai": "ClaudeAI",
        "dataengineering": "Data Engineering",
        "datascience": "Data Science",
        "localllama": "LocalLLaMA",
        "machinelearning": "Machine Learning",
        "openai": "OpenAI",
        "singularity": "Singularity",
        "stablediffusion": "Stable Diffusion"
    }
    return f"{subreddit_formats.get(subreddit.lower(), subreddit)} Subreddit"

def process_subreddit(
    genai_client: genai.Client,
    bq_client: bigquery.Client,
    subreddit: str,
    output_dir: str,
) -> bool:
    """
    Process a single subreddit's data with quota management.
    Only processes top posts to stay within API limits.

    Args:
        genai_client: The google-genai Client instance (configured for Vertex AI)
        bq_client: BigQuery client
        subreddit: Subreddit name
        output_dir: Output directory path

    Returns:
        True if processing succeeded, False otherwise
    """
    logger.info(f"Analyzing data for subreddit: {subreddit}")
    
    # Fetch data from BigQuery - get top posts by score
    # Step 1: Get top N posts ranked by score (one row per post)
    # Step 2: Join back to get comments, limited to top M comments per post
    query = """
        WITH top_posts AS (
            SELECT 
                post_id,
                MAX(post_score) AS post_score
            FROM `processed_data.joined_summary_analysis`
            WHERE LOWER(subreddit) = LOWER(@subreddit)
            GROUP BY post_id
            ORDER BY post_score DESC
            LIMIT @max_posts
        ),
        ranked_comments AS (
            SELECT 
                jsa.*,
                ROW_NUMBER() OVER (
                    PARTITION BY jsa.post_id 
                    ORDER BY jsa.sentiment_score DESC
                ) AS comment_rank
            FROM `processed_data.joined_summary_analysis` jsa
            INNER JOIN top_posts tp ON jsa.post_id = tp.post_id
            WHERE LOWER(jsa.subreddit) = LOWER(@subreddit)
        )
        SELECT 
            post_id, subreddit, post_score, post_url, comment_id,
            summary_date, post_content, comment_body, comment_summary,
            sentiment_score, sentiment_label
        FROM ranked_comments
        WHERE comment_rank <= @max_comments
        ORDER BY post_score DESC, comment_rank ASC
    """
    
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("subreddit", "STRING", subreddit),
            bigquery.ScalarQueryParameter("max_posts", "INT64", MAX_TOP_POSTS_PER_SUBREDDIT),
            bigquery.ScalarQueryParameter("max_comments", "INT64", MAX_COMMENTS_PER_POST)
        ]
    )
    
    query_job = bq_client.query(query, job_config=job_config)
    rows = list(query_job.result())

    if not rows:
        logger.info(f"No data found for subreddit: {subreddit}")
        return False
    
    # Log data reduction stats
    total_posts = len(set(row.post_id for row in rows))
    total_comments = len(rows)
    logger.info(f"Processing {total_posts} posts with {total_comments} comments for {subreddit} "
                f"(limited to top {MAX_TOP_POSTS_PER_SUBREDDIT} posts, {MAX_COMMENTS_PER_POST} comments each)")

    # Prepare prompt with limited data
    text_files = "".join(format_text_file(row) for row in rows)
    final_prompt = create_prompt_template() + text_files
    
    # Estimate token count (rough approximation: 1 token ≈ 4 characters)
    estimated_tokens = len(final_prompt) // 4
    logger.info(f"Estimated token count for {subreddit}: ~{estimated_tokens:,} tokens")

    # Make request with retry logic
    try:
        response = make_gemini_request_with_retry(genai_client, final_prompt)
        formatted_response = response.text
        
        # Replace both title and description with proper formatting
        formatted_subreddit = get_formatted_subreddit_name(subreddit)
        formatted_response = formatted_response.replace(
            f'title: "{subreddit} subreddit"',
            f'title: "{formatted_subreddit}"'
        ).replace(
            f'description: "Analysis of top discussions and trends in {subreddit} subreddit"',
            f'description: "Analysis of top discussions and trends in {formatted_subreddit}"'
        )
        
        output_file_path = os.path.join(output_dir, f"llm_{subreddit}.md")
        
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(formatted_response)
        logger.info(f"Output saved to {output_file_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error processing subreddit {subreddit}: {e}")
        return False

def clean_markdown_file(file_path):
    """
    Remove triple backticks and clean up resulting whitespace from markdown file
    while preserving markdown formatting.
    
    Args:
        file_path (str): Path to the markdown file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Clean lines and remove empty lines that resulted from backtick removal
        cleaned_lines = []
        for line in lines:
            # Remove backticks and trim whitespace
            cleaned_line = line.replace('```', '').rstrip()
            # Only add non-empty lines or lines that are intentionally blank (part of markdown)
            if cleaned_line or line.strip() == '':
                cleaned_lines.append(cleaned_line + '\n')
        
        # Write cleaned content back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)
        
        logger.info(f"Successfully cleaned markdown file: {file_path}")
    except Exception as e:
        logger.error(f"Error cleaning markdown file {file_path}: {e}")
        raise

def analyze_data():
    """
    Main function to analyze Reddit data using Google's Gemini model.
    
    Pipeline steps:
    1. Set up logging and output directory with current date
    2. Initialize Gemini model
    3. Connect to BigQuery and GCS
    4. Process each subreddit (limited to top posts to stay within quota)
    5. Clean generated markdown files
    6. Upload results to GCS
    
    Note:
        Implements quota management to avoid hitting daily API limits.
        Processes only top posts per subreddit to reduce token usage.
    """
    global request_count
    
    try:
        # 1. Set up output directory with year/month/day structure
        current_date = datetime.now()
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        day = current_date.strftime('%d')
        
        output_dir = os.path.join(CLOUD_DIR, 'results', year, month, day)
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Output directory set to {output_dir}")

        # 2. Initialize Vertex AI client (google-genai SDK)
        project_id = GCP_CONFIG["project_id"]
        region = GCP_CONFIG["region"]
        if not project_id or not region:
            raise ValueError(
                "GCP_PROJECT_ID and GCP_REGION must be set in environment for Vertex AI"
            )

        # Use the same service account credentials we use for BigQuery/GCS
        credentials = get_gcp_credentials()
        genai_client = genai.Client(
            vertexai=True,
            project=project_id,
            location=region,
            credentials=credentials,
        )
        logger.info(f"Vertex AI client initialized | project={project_id} region={region} model={GEMINI_MODEL}")
        logger.info(
            f"Limits: max {MAX_DAILY_REQUESTS} req/day, {MAX_REQUESTS_PER_MINUTE} RPM, "
            f"top {MAX_TOP_POSTS_PER_SUBREDDIT} posts/subreddit, "
            f"{MAX_COMMENTS_PER_POST} comments/post"
        )

        # 3. Connect to BigQuery and GCS
        bq_client = bigquery.Client(credentials=credentials, project=project_id)
        storage_client = storage.Client(credentials=credentials, project=project_id)
        logger.info("BigQuery and GCS clients initialized")

        # 4. Process subreddits with quota tracking
        successful_subreddits = []
        failed_subreddits = []

        for subreddit in SUBREDDITS:
            success = process_subreddit(genai_client, bq_client, subreddit, output_dir)
            if success:
                successful_subreddits.append(subreddit)
            else:
                failed_subreddits.append(subreddit)
                # If we hit quota limit, stop processing remaining subreddits
                if request_count >= MAX_DAILY_REQUESTS:
                    logger.warning(f"Quota limit reached. Skipping remaining subreddits: "
                                 f"{SUBREDDITS[SUBREDDITS.index(subreddit)+1:]}")
                    break
            
        # 5. Clean markdown files and upload to GCS
        uploaded_files = 0
        for filename in os.listdir(output_dir):
            if filename.endswith('.md'):
                local_file_path = os.path.join(output_dir, filename)
                
                # Clean the markdown file
                clean_markdown_file(local_file_path)
                
                # Upload to GCS
                gcs_blob_path = get_gcs_path(year, month, day, filename)
                upload_to_gcs(local_file_path, gcs_blob_path, storage_client)
                uploaded_files += 1

        # 6. Log final summary
        logger.info("=" * 60)
        logger.info("ANALYSIS SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Total API requests made: {request_count}/{MAX_DAILY_REQUESTS}")
        logger.info(f"Successful subreddits ({len(successful_subreddits)}): {', '.join(successful_subreddits)}")
        if failed_subreddits:
            logger.warning(f"Failed subreddits ({len(failed_subreddits)}): {', '.join(failed_subreddits)}")
        logger.info(f"Files uploaded to GCS: {uploaded_files}")
        logger.info("=" * 60)
        logger.info("Analysis complete - all files processed and uploaded to GCS")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    analyze_data() 