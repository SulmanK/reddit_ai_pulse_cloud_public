{# 
    Macro to run a specified test across all subreddit source tables
    Args:
        test_name: The name of the test to run
    Returns:
        Combined results of running the test across all subreddit tables
#}

{% macro test_all_sources(test_name) %}
    {% for subreddit in var('subreddits') %}
        {% set source_relation = source('raw_data', 'raw_' ~ subreddit) %}
        {{ test_name }}(source_relation)
    {% endfor %}
{% endmacro %}



{# 
    Test macro to validate JSON data
    Args:
        model: The dbt model to test
        column_name: The name of the column containing JSON data
    Returns:
        Records where JSON parsing fails
#}

{% macro test_is_json(model, column_name) %}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} IS NOT NULL
  AND NOT ({{ column_name }}::jsonb IS NOT NULL)
{% endmacro %}



{# 
    Test macro to validate timestamp data
    Args:
        model: The dbt model to test
        column_name: The name of the column containing timestamps
    Returns:
        Records where timestamp conversion fails
#}
{% macro test_is_timestamp(model, column_name) %}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} IS NOT NULL
  AND (
    CASE 
      WHEN {{ column_name }}::timestamp IS NULL THEN true
      ELSE false
    END
  )
{% endmacro %}


{# 
    Test macro to validate bigint data type
    Args:
        model: The dbt model to test
        column_name: The name of the column containing bigint data
    Returns:
        Records where bigint validation fails
#}

{% macro test_is_bigint(model, column_name) %}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} IS NOT NULL
  AND (
    CASE 
      WHEN {{ column_name }}::bigint IS NULL THEN true
      WHEN {{ column_name }} < -9223372036854775808 THEN true  -- Min bigint value
      WHEN {{ column_name }} > 9223372036854775807 THEN true   -- Max bigint value
      ELSE false
    END
  )
{% endmacro %}


{# 
    Test macro to validate string data type
    Args:
        model: The dbt model to test
        column_name: The name of the column containing string data
    Returns:
        Records where string validation fails (non-text data or invalid characters)
#}

{% macro test_is_string(model, column_name) %}
SELECT 
    *,
    {{ column_name }} as failed_value
FROM {{ model }}
WHERE {{ column_name }} IS NOT NULL
  AND (
    CASE 
      WHEN {{ column_name }}::text IS NULL THEN true                    -- Can't be cast to text
      WHEN LENGTH(TRIM({{ column_name }}::text)) = 0 THEN true         -- Empty strings
      WHEN {{ column_name }}::text ~ '[^\x20-\x7E\s]' THEN true        -- Contains invalid characters
      ELSE false
    END
  )
{% endmacro %}

{# 
    Test macro to validate integer data type
    Args:
        model: The dbt model to test
        column_name: The name of the column containing integer data
        min_value: Optional minimum value (default: -2147483648)
        max_value: Optional maximum value (default: 2147483647)
    Returns:
        Records where integer validation fails
#}

{% macro test_is_int(model, column_name, min_value='-2147483648', max_value='2147483647') %}
WITH validation AS (
    SELECT 
        *,
        {{ column_name }} as test_value,
        CASE
            WHEN {{ column_name }} IS NULL THEN NULL
            WHEN {{ column_name }}::text ~ '^[0-9-]+$' THEN TRUE
            ELSE FALSE
        END as is_numeric,
        CASE
            WHEN {{ column_name }} IS NULL THEN NULL
            WHEN {{ column_name }}::integer IS NULL THEN FALSE
            ELSE TRUE
        END as is_valid_int
    FROM {{ model }}
)

SELECT 
    *,
    'Failed integer validation' as failure_reason
FROM validation
WHERE {{ column_name }} IS NOT NULL
    AND (
        NOT is_numeric
        OR NOT is_valid_int
        OR test_value < {{ min_value }}
        OR test_value > {{ max_value }}
        OR test_value != FLOOR(test_value)  -- Checks if it's a whole number
    )
{% endmacro %} 



{# 
    Test macro to validate text data type with additional text-specific validations
    Args:
        model: The dbt model to test
        column_name: The name of the column containing text data
        min_length: Optional minimum text length (default: 1)
        max_length: Optional maximum text length (default: 65535)
        allow_null: Optional flag to allow NULL values (default: false)
        regex_pattern: Optional regex pattern to match (default: none)
    Returns:
        Records where text validation fails
#}

{% macro test_is_text(model, column_name, min_length=1, max_length=65535, allow_null=false, regex_pattern=none) %}
WITH validation AS (
    SELECT 
        *,
        {{ column_name }} as test_value,
        CASE
            WHEN {{ column_name }} IS NULL THEN 'NULL value'
            WHEN NOT pg_typeof({{ column_name }}) IN ('text'::regtype, 'varchar'::regtype) THEN 'Invalid type'
            WHEN LENGTH({{ column_name }}) < {{ min_length }} THEN 'Too short'
            WHEN LENGTH({{ column_name }}) > {{ max_length }} THEN 'Too long'
            {% if regex_pattern is not none %}
            WHEN NOT {{ column_name }} ~ '{{ regex_pattern }}' THEN 'Failed pattern match'
            {% endif %}
            ELSE 'VALID'
        END as validation_status,
        LENGTH({{ column_name }}) as text_length
    FROM {{ model }}
)

SELECT 
    *,
    validation_status as failure_reason,
    text_length
FROM validation
WHERE validation_status != 'VALID'
    {% if not allow_null %}
    AND (test_value IS NULL OR validation_status != 'NULL value')
    {% endif %}
{% endmacro %}