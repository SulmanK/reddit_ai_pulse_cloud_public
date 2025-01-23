{{
    config(
        materialized='view'
    )
}}

SELECT
    id,
    subreddit,
    post_id,
    post_score,
    post_url,
    comment_id,
    summary_date,
    processed_date,
    post_content,
    comment_body
FROM {{ source('summary_analytics', 'daily_summary_data') }} ds
WHERE comment_body IS NOT NULL
    AND needs_processing = TRUE