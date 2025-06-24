-- =============================================================================
-- delete_date_data.sql
-- -----------------------------------------------------------------------------
-- BigQuery Delete Script for Reddit AI Pulse Cloud Pipeline
-- 
-- Deletes all entries for June 23, 2025 (Eastern UTC timezone)
-- 
-- This script removes data from all relevant tables in the correct order
-- to maintain referential integrity:
-- 1. Analytics tables (text summaries, sentiment analysis)
-- 2. Daily summary data
-- 3. Processed posts and comments tables
-- 4. Raw subreddit data tables
-- 5. Processing metadata
--
-- Date Range: June 23, 2025 00:00:00 to 23:59:59 Eastern UTC
-- UTC Equivalent: June 23, 2025 04:00:00 to June 24, 2025 03:59:59 UTC
-- Unix Timestamp Range: 1750737600 to 1750823999
--
-- Usage: Run this script in BigQuery console or via bq command line
-- =============================================================================

-- =============================================================================
-- PHASE 1: DELETE FROM ANALYTICS TABLES
-- =============================================================================

-- Delete from text_summary_results (via comment_id relationship)
DELETE FROM `reddit-ai-pulse-2.processed_data.text_summary_results`
WHERE comment_id IN (
  SELECT DISTINCT comment_id 
  FROM `reddit-ai-pulse-2.processed_data.daily_summary_data`
  WHERE summary_date = '2025-06-23'
);

-- Delete from sentiment_analysis_results (via comment_id relationship)  
DELETE FROM `reddit-ai-pulse-2.processed_data.sentiment_analysis_results`
WHERE comment_id IN (
  SELECT DISTINCT comment_id 
  FROM `reddit-ai-pulse-2.processed_data.daily_summary_data`
  WHERE summary_date = '2025-06-23'
);

-- =============================================================================
-- PHASE 2: DELETE FROM DAILY SUMMARY DATA
-- =============================================================================

-- Delete from daily_summary_data (direct date match)
DELETE FROM `reddit-ai-pulse-2.processed_data.daily_summary_data`
WHERE summary_date = '2025-06-23';

-- =============================================================================
-- PHASE 3: DELETE FROM PROCESSED TABLES (COMMENTS AND POSTS)
-- =============================================================================

-- Delete from comments tables for each subreddit
DELETE FROM `reddit-ai-pulse-2.processed_data.comments_dataengineering`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.comments_datascience`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.comments_machinelearning`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.comments_claudeai`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.comments_singularity`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.comments_localllama`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.comments_openai`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.comments_stablediffusion`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

-- Delete from posts tables for each subreddit
DELETE FROM `reddit-ai-pulse-2.processed_data.posts_dataengineering`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.posts_datascience`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.posts_machinelearning`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.posts_claudeai`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.posts_singularity`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.posts_localllama`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.posts_openai`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

DELETE FROM `reddit-ai-pulse-2.processed_data.posts_stablediffusion`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

-- =============================================================================
-- PHASE 4: DELETE FROM RAW DATA TABLES
-- =============================================================================

-- Delete from raw subreddit tables (using Unix timestamp in FLOAT format)
DELETE FROM `reddit-ai-pulse-2.raw_data.raw_dataengineering`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

DELETE FROM `reddit-ai-pulse-2.raw_data.raw_datascience`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

DELETE FROM `reddit-ai-pulse-2.raw_data.raw_machinelearning`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

DELETE FROM `reddit-ai-pulse-2.raw_data.raw_claudeai`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

DELETE FROM `reddit-ai-pulse-2.raw_data.raw_singularity`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

DELETE FROM `reddit-ai-pulse-2.raw_data.raw_localllama`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

DELETE FROM `reddit-ai-pulse-2.raw_data.raw_openai`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

DELETE FROM `reddit-ai-pulse-2.raw_data.raw_stablediffusion`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;

-- =============================================================================
-- PHASE 5: UPDATE PROCESSING METADATA (OPTIONAL)
-- =============================================================================

-- Optionally reset processing metadata for affected subreddits if needed
-- This ensures the pipeline can reprocess data for this date range
-- Uncomment the following lines if you want to reset the last processed timestamps

/*
UPDATE `reddit-ai-pulse-2.processed_data.processing_metadata`
SET 
  last_processed_timestamp = 1750737599.0,  -- Set to just before our deleted range
  last_update_time = CURRENT_TIMESTAMP()
WHERE subreddit IN (
  'dataengineering', 'datascience', 'machinelearning', 'claudeai',
  'singularity', 'localllama', 'openai', 'stablediffusion'
);
*/

-- =============================================================================
-- VERIFICATION QUERIES (OPTIONAL - FOR MANUAL VERIFICATION)
-- =============================================================================

/*
-- Uncomment to verify deletion was successful

-- Check remaining records in daily_summary_data for the target date
SELECT COUNT(*) as remaining_summary_records
FROM `reddit-ai-pulse-2.processed_data.daily_summary_data`
WHERE summary_date = '2025-06-23';

-- Check remaining records in a sample processed table
SELECT COUNT(*) as remaining_processed_records
FROM `reddit-ai-pulse-2.processed_data.posts_dataengineering`
WHERE created_utc >= '2025-06-23 04:00:00 UTC' AND created_utc <= '2025-06-24 03:59:59 UTC';

-- Check remaining records in a sample raw table
SELECT COUNT(*) as remaining_raw_records
FROM `reddit-ai-pulse-2.raw_data.raw_dataengineering`
WHERE created_utc >= 1750737600.0 AND created_utc <= 1750823999.0;
*/

-- =============================================================================
-- EXECUTION COMPLETE
-- =============================================================================

SELECT 'Data deletion completed for June 23, 2025 (Eastern UTC)' as status,
       CURRENT_TIMESTAMP() as completion_time; 