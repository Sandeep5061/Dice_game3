from __future__ import annotations

from .models import AnalyzedJob, CandidateProfile


def tailor_resume(profile: CandidateProfile, analyzed: AnalyzedJob) -> str:
    matched = ", ".join(analyzed.matched_skills) or "general software engineering"
    return (
        f"{profile.name}\n"
        f"Email: {profile.email} | Phone: {profile.phone}\n\n"
        "Summary\n"
        f"Engineer with strengths in {', '.join(profile.skills)}.\n"
        f"Targeted for {analyzed.posting.title} at {analyzed.posting.company}.\n\n"
        "Role fit\n"
        f"Matched capabilities for this role: {matched}.\n"
    )


def generate_cover_letter(profile: CandidateProfile, analyzed: AnalyzedJob) -> str:
    return (
        f"Dear Hiring Manager at {analyzed.posting.company},\n\n"
        f"I am excited to apply for the {analyzed.posting.title} role in {analyzed.posting.location}. "
        f"My background in {', '.join(profile.skills)} aligns with your needs. "
        f"I am particularly confident due to my experience with {', '.join(analyzed.matched_skills) or 'modern software delivery'}.\n\n"
        "Thank you for your consideration.\n"
        f"Sincerely,\n{profile.name}"
    )
