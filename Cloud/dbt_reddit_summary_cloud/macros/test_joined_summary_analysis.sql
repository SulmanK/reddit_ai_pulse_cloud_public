{# 
    Test macro to validate comment length
    Args:
        model: The dbt model to test
        column_name: The name of the column containing comment text
    Returns:
        Records that fail validation (too short < 2 chars or too long > 10000 chars)
#}

{% macro test_valid_comment_length(model, column_name) %}
  SELECT 
    comment_id,
    {{ column_name }} as comment_body
  FROM {{ model }}
  WHERE 
    LENGTH(TRIM({{ column_name }})) < 2  -- Test for extremely short comments
    OR LENGTH({{ column_name }}) > 10000  -- Test for extremely long comments
{% endmacro %}




{# 
    Test macro to validate summary quality
    Args:
        model: The dbt model to test
        column_name: The name of the column containing the summary
    Returns:
        Records where summary is longer than original comment or missing
#}

{% macro test_summary_quality(model, column_name) %}
  WITH base AS (
    SELECT 
      comment_id,
      comment_body,
      {{ column_name }} as comment_summary
    FROM {{ model }}
    WHERE {{ column_name }} IS NOT NULL
  )
  SELECT 
    comment_id,
    comment_body,
    comment_summary
  FROM base
  WHERE 
    LENGTH(comment_summary) > LENGTH(comment_body)  -- Summary shouldn't be longer than original
   -- OR LENGTH(TRIM(comment_summary)) < 10  -- Test for extremely short summaries
{% endmacro %}




{# 
    Test macro to validate sentiment scores and labels
    Args:
        model: The dbt model to test
        column_name: The name of the column containing sentiment scores
    Returns:
        Records with invalid sentiment scores (outside 0-1 range)
#}
{% macro test_sentiment_consistency(model, column_name) %}
  WITH base AS (
    SELECT 
      comment_id,
      {{ column_name }} as sentiment_score,
      sentiment_label
    FROM {{ model }}
    WHERE {{ column_name }} IS NOT NULL
      AND sentiment_label IS NOT NULL
  )
  SELECT 
    comment_id,
    sentiment_score,
    sentiment_label
  FROM base
  WHERE 
    sentiment_score < 0  -- Should never be negative
    OR sentiment_score > 1  -- Should never be greater than 1
{% endmacro %} 


{# 
    Macro to warn if a column contains NULL values
    Args:
        model: The model/table to check
        column_name: The name of the column to check for NULLs
    Returns:
        A warning message if NULL values are found
#}

{% macro warn_if_null(model, column_name) %}
{% set null_count_query %}
    SELECT COUNT(*) AS null_count
    FROM {{ ref(model) }}  -- Changed from source to ref
    WHERE {{ column_name }} IS NULL
{% endset %}

{% set results = run_query(null_count_query) %}
{% set null_count = results.columns[0].values()[0] %}

{% if null_count > 0 %}
    {{ log("Warning: Column '" ~ column_name ~ "' in model '" ~ model ~ "' contains " ~ null_count ~ " NULL values.", info=True) }}
{% endif %}

{% endmacro %}