from __future__ import annotations

from .models import AnalyzedJob, CandidateProfile, JobPosting


def analyze_job(posting: JobPosting, profile: CandidateProfile, min_match_score: float) -> AnalyzedJob:
    text = f"{posting.title} {posting.description}".lower()
    skills = [s.lower() for s in profile.skills]

    matched = [skill for skill in skills if skill in text]
    missing = [skill for skill in skills if skill not in text]
    score = len(matched) / max(len(skills), 1)

    return AnalyzedJob(
        posting=posting,
        match_score=round(score, 2),
        matched_skills=matched,
        missing_skills=missing,
        should_apply=score >= min_match_score,
    )
