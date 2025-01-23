{{ config(
    materialized='table',
    unique_key='comment_id',
) }}

WITH validation_cte AS (
    SELECT 
        cs.*,
        ts.comment_summary,
        sa.sentiment_score,
        sa.sentiment_label,
        CASE 
            WHEN LENGTH(cs.comment_body) < 2 THEN 'Too short'
            WHEN LENGTH(cs.comment_body) > 10000 THEN 'Too long'
            ELSE 'Valid'
        END as comment_quality,
        CASE 
            WHEN ts.comment_summary IS NULL OR TRIM(ts.comment_summary) = '' THEN 'Missing'
            WHEN LENGTH(ts.comment_summary) > LENGTH(cs.comment_body) THEN 'Invalid'
            ELSE 'Valid'
        END as summary_quality
    FROM {{ source('summary_analytics', 'current_summary_staging') }} cs
    LEFT JOIN {{ source('summary_analytics', 'text_summary_results') }} ts 
        ON cs.comment_id = ts.comment_id
    LEFT JOIN {{ source('summary_analytics', 'sentiment_analysis_results') }} sa 
        ON cs.comment_id = sa.comment_id
)

SELECT 
    *,
    CURRENT_TIMESTAMP as processed_at,
    'dbt' as processed_by
FROM validation_cte
WHERE comment_quality = 'Valid' 
  AND summary_quality = 'Valid'