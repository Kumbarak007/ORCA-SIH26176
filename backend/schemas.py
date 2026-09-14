from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Location:
    latitude: float
    longitude: float


@dataclass
class MissionConstraints:
    avoid_high_wind: bool = True
    avoid_unsafe_sea: bool = True
    avoid_restricted_areas: bool = True
    max_wave_height: float | None = None


@dataclass
class MissionPreferences:
    maximize_fishing_potential: bool = True
    minimize_risk: bool = True
    minimize_travel_distance: bool = True
    primary_preference: str = "balanced"


@dataclass
class Mission:
    objective: str
    location: str
    departure_time: str
    fishing_duration_hours: float | None
    return_deadline: str

    constraints: MissionConstraints = field(
        default_factory=MissionConstraints
    )

    preferences: MissionPreferences = field(
        default_factory=MissionPreferences
    )


@dataclass
class Evidence:
    source: str
    zone_id: str
    variable: str
    value: float | str

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    unit: Optional[str] = None
    timestamp: Optional[str] = None
    confidence: float = 1.0
    explanation: Optional[str] = None


@dataclass
class CandidatePlan:
    plan_id: str
    zone_id: str
    score: float
    feasible: bool

    rejection_reasons: list[str] = field(
        default_factory=list
    )

    evidence: list[Evidence] = field(
        default_factory=list
    )


@dataclass
class Recommendation:
    selected_plan_id: str | None
    zone_id: str | None
    score: float
    status: str
    rationale: str
    evidence: list[Evidence] = field(default_factory=list)
    rejected_plans: list[CandidatePlan] = field(default_factory=list)