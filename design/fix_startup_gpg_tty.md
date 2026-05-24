# Fix: VM Startup Script GPG TTY Failure + BigQuery Backlog Recovery

## Status
🔧 In Progress

## Problem Statement

Since May 17, 2026, the pipeline has produced zero Gemini output files. The VM starts daily
(via Cloud Scheduler) but the startup script exits with error code 2 after ~1 minute, before
Docker, git, or Airflow ever run. The root cause is:

```
gpg: cannot open '/dev/tty': No such device or address
(23) Failed writing body
Script "startup-script" failed with error: exit status 2
```

The startup script installs Docker using `curl ... | gpg --dearmor -o docker.gpg`. Since the
GCE metadata script runner updated (to `progVersion: "20260228.00"`) it no longer allocates a
pseudo-TTY to startup scripts. `gpg --dearmor` tries to open `/dev/tty` in newer GPG versions
even for non-interactive operations and fails. With `set -e` + `set -o pipefail` active, the
script exits immediately, leaving the VM idle until Cloud Scheduler stops it.

**Secondary effect:** 3,551 BigQuery records (May 16–23) accumulated with `needs_processing = TRUE`
and were not present in the `update_processing_status` table — meaning no summarization, sentiment
analysis, or Gemini output was produced for this data.

## Root Cause Chain

```
GCE metadata runner update
  → gpg loses /dev/tty access
    → startup.sh exits at Docker GPG setup step (set -e)
      → Docker never installed / Airflow never started
        → Pipeline never runs
          → needs_processing stuck = TRUE (3,551 records)
            → No GCS output files since May 16
```

## Fix

### Part 1: `startup.sh` — Two-pronged hardening

**Fix A — Idempotent Docker install:** Wrap the entire Docker setup block in an
`if ! command -v docker` guard. On a fresh VM, Docker installs normally. On subsequent
boots (where Docker is already on the persistent disk), the block is skipped entirely,
eliminating the gpg issue going forward.

**Fix B — Remove gpg dependency:** Replace the `curl | gpg --dearmor` pattern with the
modern Docker-recommended approach of saving the key as an ASCII-armored `.asc` file
directly. This removes any gpg involvement entirely:

```bash
# Old (broken):
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# New (no gpg needed):
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc
# signed-by in the apt source line updated to reference docker.asc
```

The combination of both fixes means:
- **Fresh VM**: Docker installed using the gpg-free method — no TTY issue possible
- **Rebooted VM**: Docker block skipped entirely — zero risk

### Part 2: BigQuery backlog reset (applied immediately, out of band)

Reset the 3,551 stuck records so new daily ingestion proceeds normally:

```sql
UPDATE `reddit-ai-pulse-6.processed_data.daily_summary_data`
SET needs_processing = FALSE
WHERE needs_processing = TRUE
  AND DATE(summary_date) < CURRENT_DATE();
```

**Trade-off:** The 7 days of backlogged data (May 16–23) are skipped rather than backfilled.
Given these are time-sensitive daily pulse summaries, stale data provides limited value.
A backfill run could be done separately if desired.

## Files Changed

| File | Change |
|------|--------|
| `Cloud/infrastructure/terraform/vm_scripts/startup.sh` | Wrap Docker install in `if ! docker` guard; replace `gpg --dearmor` with `.asc` download |

## Deployment Steps

1. ✅ BigQuery data fix applied (3,551 records reset)
2. Merge PR to `main`
3. Run `build_res.sh` to push updated `startup.sh` to VM metadata
4. On next scheduled VM start (4PM EST), confirm startup completes successfully via Cloud Logging

## Verification

- Cloud Logging shows no `gpg: cannot open '/dev/tty'` error
- Cloud Logging shows `Startup script completed successfully`
- `needs_processing` count stays at 0 after the next pipeline run
- GCS results folder updated with new Gemini output
