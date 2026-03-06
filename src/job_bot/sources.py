from __future__ import annotations

from typing import List

from .models import CandidateProfile, JobPosting


SAMPLE_JOBS = [
    JobPosting(
        source="LinkedIn",
        title="Java Backend Engineer",
        company="Acme Cloud",
        location="Bengaluru",
        url="https://example.com/linkedin/1",
        description="Build Spring Boot microservices, Kafka pipelines, Docker deployment, and REST APIs.",
    ),
    JobPosting(
        source="Indeed",
        title="Frontend React Developer",
        company="Pixel Labs",
        location="Remote",
        url="https://example.com/indeed/2",
        description="Develop React UI, TypeScript components, and dashboard analytics views.",
    ),
    JobPosting(
        source="Wellfound",
        title="Full Stack Engineer",
        company="Stealth Startup",
        location="Hyderabad",
        url="https://example.com/wellfound/3",
        description="Own backend APIs in Java and frontend features in React. Build tests and CI.",
    ),
    JobPosting(
        source="Naukri.com",
        title="Data Analyst",
        company="FinEdge",
        location="Pune",
        url="https://example.com/naukri/4",
        description="PowerBI and SQL heavy reporting role with little software engineering.",
    ),
]


def search_jobs(profile: CandidateProfile, max_jobs: int) -> List[JobPosting]:
    """Simple, deterministic search provider so the project is runnable locally.

    Filters by preferred location when possible and returns at most max_jobs.
    """
    loc_set = {loc.lower() for loc in profile.locations}
    preferred = [j for j in SAMPLE_JOBS if j.location.lower() in loc_set or j.location.lower() == "remote"]
    jobs = preferred or SAMPLE_JOBS
    return jobs[:max_jobs]
