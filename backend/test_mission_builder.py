from mission_parser import MissionParser
from mission_builder import MissionBuilder


parser = MissionParser()
builder = MissionBuilder()

user_mission = (
    "I want to go fishing near Goa tomorrow morning "
    "for 5 hours. Avoid high wind and restricted areas."
)

parsed_data = parser.parse_mission(user_mission)

mission = builder.build_mission(parsed_data)


print("\n===== ORCA MISSION BUILDER TEST =====\n")

print("Builder:", builder.name)

print("\nMission Object:")
print("Objective:", mission.objective)
print("Location:", mission.location)
print("Departure Time:", mission.departure_time)
print("Fishing Duration:", mission.fishing_duration_hours)
print("Return Deadline:", mission.return_deadline)

print("\nMission Constraints:")
print("Avoid High Wind:", mission.constraints.avoid_high_wind)
print("Avoid Unsafe Sea:", mission.constraints.avoid_unsafe_sea)
print(
    "Avoid Restricted Areas:",
    mission.constraints.avoid_restricted_areas
)

print("\nMission Preferences:")
print(
    "Maximize Fishing Potential:",
    mission.preferences.maximize_fishing_potential
)
print(
    "Minimize Risk:",
    mission.preferences.minimize_risk
)
print(
    "Minimize Travel Distance:",
    mission.preferences.minimize_travel_distance
)

print("\n===== TEST PASSED =====")