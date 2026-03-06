from __future__ import annotations

from .models import ApplicationStatus, JobPosting


def apply_to_job(posting: JobPosting) -> tuple[ApplicationStatus, str]:
    """Deterministic simulated apply step.

    Real portals require authenticated sessions and anti-bot safeguards,
    so this project keeps a local-safe implementation while preserving
    the production pipeline contract.
    """
    easy_apply_sources = {"LinkedIn", "Indeed", "Wellfound", "Naukri.com"}
    if posting.source in easy_apply_sources:
        return ApplicationStatus.APPLIED, "Simulated Easy Apply submitted"
    return ApplicationStatus.FAILED, "Unsupported source"
