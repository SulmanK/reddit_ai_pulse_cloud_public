"""
Tests that Vertex AI Gemini access works using the exact same credential
flow as gemini_analyzer.py (service account file with explicit
cloud-platform scope, or ADC with that scope as a local fallback).

This verifies the fix for:
    invalid_scope: Invalid OAuth scope or ID token audience provided.

Usage: python test_gemini.py
"""

import os
import sys
import time
from dotenv import load_dotenv

ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Cloud", ".env")
load_dotenv(ENV_PATH)

try:
    from google import genai
except ImportError:
    print("ERROR: google-genai SDK not installed.")
    print("Run: pip install google-genai python-dotenv")
    sys.exit(1)

VERTEX_SCOPE = "https://www.googleapis.com/auth/cloud-platform"


def build_credentials():
    """
    Build Vertex AI credentials the same way gemini_analyzer.py does:
      1. Service account file + explicit cloud-platform scope  (production)
      2. ADC + explicit cloud-platform scope                   (local dev)
    """
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    if creds_path and os.path.exists(creds_path):
        from google.oauth2 import service_account
        creds = service_account.Credentials.from_service_account_file(
            creds_path, scopes=[VERTEX_SCOPE]
        )
        print(f"Auth:        service account file (scoped to cloud-platform)")
        print(f"  Path:      {creds_path}")
        return creds
    else:
        import google.auth
        if creds_path:
            print(f"NOTE: SA file not found at {creds_path} — using ADC")
        # Temporarily unset GOOGLE_APPLICATION_CREDENTIALS so google.auth.default()
        # uses gcloud ADC instead of trying (and failing) to load the missing file.
        saved = os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)
        try:
            creds, _ = google.auth.default(scopes=[VERTEX_SCOPE])
        finally:
            if saved:
                os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = saved
        print(f"Auth:        ADC (scoped to cloud-platform)")
        return creds


def test_model(client: "genai.Client", model_name: str) -> dict:
    """Make a simple generate_content call and record success/failure."""
    result = {"model": model_name, "success": False, "response": None,
              "error": None, "duration_ms": 0}
    try:
        start = time.time()
        response = client.models.generate_content(
            model=model_name,
            contents="Say 'Hello from Vertex AI!' and nothing else.",
        )
        result["duration_ms"] = int((time.time() - start) * 1000)
        result["success"] = True
        result["response"] = response.text.strip() if response.text else "(empty)"
    except Exception as e:
        result["error"] = str(e)
    return result


def main():
    project_id = os.getenv("GCP_PROJECT_ID")
    region = os.getenv("GCP_REGION", "us-central1")

    if not project_id:
        print("ERROR: GCP_PROJECT_ID not found in .env")
        sys.exit(1)

    print(f"Project ID:  {project_id}")
    print(f"Region:      {region}")
    print(f"Loaded from: {ENV_PATH}")
    print("=" * 70)

    # Build credentials — mirrors gemini_analyzer.py exactly
    try:
        credentials = build_credentials()
    except Exception as e:
        print(f"ERROR: Failed to build credentials: {e}")
        sys.exit(1)

    # Initialize client with those credentials
    try:
        client = genai.Client(
            vertexai=True,
            project=project_id,
            location=region,
            credentials=credentials,
        )
        print("Vertex AI client initialized successfully\n")
    except Exception as e:
        print(f"ERROR: Failed to initialize Vertex AI client: {e}")
        sys.exit(1)

    # Test models
    models_to_test = ["gemini-2.5-flash-lite", "gemini-2.5-flash"]
    results = []
    for model_name in models_to_test:
        print(f"Testing {model_name}...")
        result = test_model(client, model_name)
        results.append(result)
        if result["success"]:
            print(f"  SUCCESS ({result['duration_ms']}ms)")
            print(f"  Response: {result['response']}")
        else:
            print(f"  FAILED")
            print(f"  Error: {result['error'][:300]}")
        print()
        time.sleep(1)

    # Summary
    print("=" * 70)
    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]
    print(f"Result: {len(successful)}/{len(results)} models working")
    for r in successful:
        print(f"  OK  {r['model']} ({r['duration_ms']}ms)")
    for r in failed:
        print(f"  ERR {r['model']}")
    print("=" * 70)

    if not successful:
        print("\nAll models failed — check IAM roles and Vertex AI API enablement.")
        sys.exit(1)
    else:
        print("\nVertex AI is working. The pipeline is ready to run.")


if __name__ == "__main__":
    main()
