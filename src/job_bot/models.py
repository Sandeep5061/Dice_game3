from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
from typing import List


class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    SKIPPED = "skipped"
    FAILED = "failed"


@dataclass
class CandidateProfile:
    name: str
    email: str
    phone: str
    resume_text: str
    skills: List[str]
    locations: List[str]


@dataclass
class JobPosting:
    source: str
    title: str
    company: str
    location: str
    url: str
    description: str


@dataclass
class AnalyzedJob:
    posting: JobPosting
    match_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    should_apply: bool


@dataclass
class ApplicationResult:
    analyzed: AnalyzedJob
    tailored_resume: str
    cover_letter: str
    status: ApplicationStatus
    reason: str
    applied_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class RunRequest:
    profile: CandidateProfile
    max_jobs: int = 20
    min_match_score: float = 0.45


@dataclass
class RunResponse:
    total_scanned: int
    total_applied: int
    total_skipped: int
    results: List[ApplicationResult]

    def to_dict(self) -> dict:
        return asdict(self)
