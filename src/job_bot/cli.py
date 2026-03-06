from __future__ import annotations

import json
from dataclasses import asdict

from .engine import run_pipeline
from .models import CandidateProfile, RunRequest


def main() -> None:
    profile = CandidateProfile(
        name="Demo Candidate",
        email="demo@example.com",
        phone="+91-9999999999",
        resume_text="Experienced Java backend engineer with Spring Boot, React, Kafka and cloud delivery.",
        skills=["Java", "Spring Boot", "React", "Kafka"],
        locations=["Bengaluru", "Hyderabad", "Remote"],
    )
    request = RunRequest(profile=profile, max_jobs=10, min_match_score=0.25)
    response = run_pipeline(request)
    print(json.dumps(asdict(response), indent=2, default=str))


if __name__ == "__main__":
    main()
