# Phase 4 Test Plan: Local Component Setup and Testing

## Overview
This phase focuses on setting up and testing each component of the Reddit AI Pipeline locally using a virtual environment before containerization. This approach allows us to verify each component's functionality independently.

## Prerequisites
- Python virtual environment with dependencies installed from `combed_requirements_base.txt`
- GCP credentials configured locally
- Access to necessary APIs (Reddit, Google Cloud, etc.)

## 1. Ingest and Preprocess Testing
### Setup
1. Configure Reddit API credentials in environment
2. Set up GCS bucket connections
3. Verify BigQuery dataset access

### Test Cases
- Test Reddit data fetching for different subreddits
- Verify data preprocessing pipeline
- Validate data schema conformity
- Check error handling for API limits
- Verify data storage in GCS and BigQuery

## 2. DBT Setup and Testing
### Setup
1. Initialize DBT project structure
2. Configure BigQuery connection
3. Set up DBT profiles

### Test Cases
- Test model compilation
- Verify transformations
- Check incremental processing
- Validate data quality tests
- Test documentation generation

## 3. Summarization Component
### Setup
1. Configure necessary ML models
2. Set up text processing pipeline

### Test Cases
- Test text extraction from preprocessed data
- Verify summarization quality
- Check handling of different text lengths
- Validate output format
- Test error handling for edge cases

## 4. Sentiment Analysis
### Setup
1. Configure sentiment analysis model
2. Set up preprocessing pipeline

### Test Cases
- Test sentiment scoring accuracy
- Verify handling of different text types
- Check score normalization
- Test batch processing capability
- Validate error handling

## 5. Gemini Analyzer
### Setup
1. Configure Gemini API access
2. Set up prompt templates
3. Configure output parsing

### Test Cases
- Test prompt effectiveness
- Verify response parsing
- Check rate limiting handling
- Test error recovery
- Validate output format consistency

## Success Criteria
1. Each component successfully processes a test dataset
2. Data flows correctly between components
3. Error handling works as expected
4. Performance meets basic requirements
5. Output formats match specifications

## Test Data
- Create a small test dataset covering various scenarios
- Include edge cases and potential error conditions
- Use real subreddit data for end-to-end testing

## Monitoring and Logging
1. Set up basic logging for each component
2. Configure error tracking
3. Implement performance monitoring

## Next Steps
After successful local testing:
1. Document any configuration changes needed
2. Note performance bottlenecks
3. Identify areas needing optimization
4. Prepare for containerization

## Timeline
- Ingest/Preprocess Setup: 2 days
- DBT Setup: 1 day
- Summarization Setup: 1 day
- Sentiment Analysis Setup: 1 day
- Gemini Analyzer Setup: 1 day
- Integration Testing: 1 day

Total Estimated Time: 7 days 