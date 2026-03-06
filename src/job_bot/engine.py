from __future__ import annotations

from .analyzer import analyze_job
from .apply import apply_to_job
from .generator import generate_cover_letter, tailor_resume
from .models import ApplicationResult, ApplicationStatus, RunRequest, RunResponse
from .sources import search_jobs


def run_pipeline(request: RunRequest) -> RunResponse:
    jobs = search_jobs(request.profile, request.max_jobs)
    results: list[ApplicationResult] = []

    for job in jobs:
        analyzed = analyze_job(job, request.profile, request.min_match_score)

        if not analyzed.should_apply:
            results.append(
                ApplicationResult(
                    analyzed=analyzed,
                    tailored_resume="",
                    cover_letter="",
                    status=ApplicationStatus.SKIPPED,
                    reason="Below minimum match score",
                )
            )
            continue

        resume = tailor_resume(request.profile, analyzed)
        letter = generate_cover_letter(request.profile, analyzed)
        status, reason = apply_to_job(job)
        results.append(
            ApplicationResult(
                analyzed=analyzed,
                tailored_resume=resume,
                cover_letter=letter,
                status=status,
                reason=reason,
            )
        )

    total_applied = sum(1 for r in results if r.status == ApplicationStatus.APPLIED)
    total_skipped = sum(1 for r in results if r.status == ApplicationStatus.SKIPPED)

    return RunResponse(
        total_scanned=len(jobs),
        total_applied=total_applied,
        total_skipped=total_skipped,
        results=results,
    )
