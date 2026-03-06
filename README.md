# AI Job Application Bot

This repository implements the requirement from the shared chat as a **functional end-to-end MVP**:

- Job search across sample sources representing LinkedIn, Indeed, Naukri, and Wellfound.
- JD analysis and match scoring.
- Resume tailoring and cover-letter generation.
- Auto-apply step (simulated but wired as a real module boundary).
- Tracker-style aggregated response.
- HTTP API endpoint to run the full pipeline.

## Quick start

```bash
python -m job_bot.cli
```

Run API:

```bash
PYTHONPATH=src python -m job_bot.api
```

## Example API request

```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "profile": {
      "name": "Jane Doe",
      "email": "jane@example.com",
      "phone": "+91-9000000000",
      "resume_text": "Senior engineer with Java, Spring Boot, React, and Kafka experience.",
      "skills": ["Java", "Spring Boot", "React", "Kafka"],
      "locations": ["Bengaluru", "Remote"]
    },
    "max_jobs": 20,
    "min_match_score": 0.3
  }'
```

## Notes on real-world deployment

The `apply_to_job` module is intentionally safe and deterministic. Replacing it with real Playwright automation is straightforward, but live portals require authentication, anti-bot handling, and legal/ToS checks.
