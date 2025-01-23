{{ config(
    materialized='incremental',
    unique_key=['comment_id', 'post_id'],
    post_hook=[
        """
        UPDATE {{ source('summary_analytics', 'daily_summary_data') }}
        SET needs_processing = FALSE
        WHERE comment_id IN (
            SELECT comment_id 
            FROM {{ this }}
        );
        """
    ]
) }}

-- Select all records that were attempted to be processed, including failed validations
WITH validation_cte AS (
    SELECT 
        comment_id,
        comment_body,
        post_id
    FROM {{ source('summary_analytics', 'current_summary_staging') }}
),
all_processed_records AS (
    SELECT 
        cs.comment_id,
        cs.post_id,
        v.comment_quality
    FROM {{ source('summary_analytics', 'current_summary_staging') }} cs
    LEFT JOIN (
        SELECT 
            comment_id,
            CASE 
                WHEN LENGTH(comment_body) < 2 THEN 'Too short'
                WHEN LENGTH(comment_body) > 10000 THEN 'Too long'
                ELSE 'Valid'
            END as comment_quality
        FROM validation_cte
    ) v ON cs.comment_id = v.comment_id
)

SELECT 
    comment_id,
    post_id
FROM all_processed_records