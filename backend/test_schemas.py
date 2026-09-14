from schemas import (
    Location,
    Mission,
    MissionConstraints,
    MissionPreferences
)


mission = Mission(
    objective="fishing",

    location=Location(
        latitude=15.20,
        longitude=73.95
    ),

    departure_time="06:00",
    fishing_duration_hours=5,
    return_deadline="16:00",

    constraints=MissionConstraints(
        avoid_high_wind=True,
        avoid_unsafe_sea=True,
        avoid_restricted_areas=True
    ),

    preferences=MissionPreferences(
        maximize_fishing_potential=True,
        minimize_risk=True,
        minimize_travel_distance=True
    )
)


print("ORCA Mission")
print("--------------------")
print(mission)