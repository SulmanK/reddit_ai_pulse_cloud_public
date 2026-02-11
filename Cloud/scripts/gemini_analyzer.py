"""
Gemini Analysis Module for Cloud Environment

This module uses Google's Gemini AI to analyze Reddit data, generating insights
and summaries from processed posts and comments in BigQuery.

Owner: Sulman Khan
"""

import os
import sys
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv
from google.cloud import bigquery
from google.cloud import storage
from typing import Dict

# Add the Cloud directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUD_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(CLOUD_DIR)

from config.config import SUBREDDITS, GCS_BUCKET_NAME, GEMINI_CONFIG
from utils.custom_logging import get_logger, setup_logging

# Configure logging with absolute path
LOGS_DIR = os.path.join(CLOUD_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)
logger = setup_logging(script_name='gemini_analyzer', log_dir=LOGS_DIR)


# Constants
RESULTS_PREFIX = "results"


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

def process_subreddit(model, client, subreddit, output_dir):
    """Process a single subreddit's data."""
    logger.info(f"Analyzing data for subreddit: {subreddit}")
    
    # Fetch data from BigQuery
    query = """
        SELECT post_id, subreddit, post_score, post_url, comment_id,
               summary_date, post_content, comment_body, comment_summary,
               sentiment_score, sentiment_label
        FROM `processed_data.joined_summary_analysis`
        WHERE LOWER(subreddit) = LOWER(@subreddit)
        ORDER BY post_score DESC
    """
    
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("subreddit", "STRING", subreddit)
        ]
    )
    
    query_job = client.query(query, job_config=job_config)
    rows = list(query_job.result())

    if not rows:
        logger.info(f"No data found for subreddit: {subreddit}")
        return

    # Prepare prompt
    text_files = "".join(format_text_file(row) for row in rows)
    final_prompt = create_prompt_template() + text_files

    # Format the response after getting it from Gemini
    try:
        response = model.generate_content(final_prompt)
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
        
    except Exception as e:
        logger.error(f"Error processing subreddit {subreddit}: {e}")

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
    4. Process each subreddit
    5. Clean generated markdown files
    6. Upload results to GCS
    """
    try:
        # 1. Set up output directory with year/month/day structure
        current_date = datetime.now()
        year = current_date.strftime('%Y')
        month = current_date.strftime('%m')
        day = current_date.strftime('%d')
        
        output_dir = os.path.join(CLOUD_DIR, 'results', year, month, day)
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Output directory set to {output_dir}")

        # 2. Initialize model
        genai.configure(api_key=GEMINI_CONFIG['GOOGLE_GEMINI_API_KEY'])
        model = genai.GenerativeModel('gemini-2.5-flash')
        logger.info("Model loaded")

        # 3. Connect to BigQuery and GCS
        bq_client = bigquery.Client()
        storage_client = storage.Client()
        logger.info("BigQuery and GCS clients initialized")

        # 4. Process subreddits
        for subreddit in SUBREDDITS:
            process_subreddit(model, bq_client, subreddit, output_dir)
            
        # 5. Clean markdown files and upload to GCS
        for filename in os.listdir(output_dir):
            if filename.endswith('.md'):
                local_file_path = os.path.join(output_dir, filename)
                
                # Clean the markdown file
                clean_markdown_file(local_file_path)
                
                # Upload to GCS
                gcs_blob_path = get_gcs_path(year, month, day, filename)
                upload_to_gcs(local_file_path, gcs_blob_path, storage_client)

        logger.info("Analysis complete - all files processed and uploaded to GCS")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    analyze_data() 