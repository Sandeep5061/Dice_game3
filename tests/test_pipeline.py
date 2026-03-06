from job_bot.engine import run_pipeline
from job_bot.models import CandidateProfile, RunRequest


def test_pipeline_applies_to_matching_jobs() -> None:
    request = RunRequest(
        profile=CandidateProfile(
            name="Test",
            email="test@example.com",
            phone="123",
            resume_text="Experienced Java and Spring Boot developer with React and Kafka exposure.",
            skills=["Java", "Spring Boot", "React"],
            locations=["Remote", "Bengaluru"],
        ),
        max_jobs=10,
        min_match_score=0.3,
    )

    result = run_pipeline(request)

    assert result.total_scanned > 0
    assert result.total_applied >= 1
    assert all(r.analyzed.match_score >= 0 for r in result.results)


def test_pipeline_skips_when_threshold_too_high() -> None:
    request = RunRequest(
        profile=CandidateProfile(
            name="Test",
            email="test@example.com",
            phone="123",
            resume_text="Experienced Java developer with Spring Boot and Kafka.",
            skills=["GoLang", "Rust"],
            locations=["Remote"],
        ),
        max_jobs=10,
        min_match_score=0.95,
    )

    result = run_pipeline(request)

    assert result.total_applied == 0
    assert result.total_skipped == result.total_scanned
