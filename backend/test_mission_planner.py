from mission_parser import MissionParser
from mission_builder import MissionBuilder
from mission_planner import MissionPlanner


parser = MissionParser()
builder = MissionBuilder()
planner = MissionPlanner()


user_mission = (
    "I want to go fishing near Goa tomorrow morning "
    "for 5 hours. Avoid high wind and restricted areas."
)


# 1. Parse natural-language mission
parsed_data = parser.parse_mission(user_mission)


# 2. Build ORCA Mission object
mission = builder.build_mission(parsed_data)


# 3. Ask the LLM planner which agents are relevant
plan = planner.plan(mission)


print("\n===== ORCA MISSION PLANNER TEST =====\n")

print("Planner:", planner.name)

print("\nMission:")
print("Objective:", mission.objective)
print("Location:", mission.location)
print("Departure:", mission.departure_time)
print("Duration:", mission.fishing_duration_hours)

print("\nSelected Agents:")
for agent in plan["selected_agents"]:
    print(f"  - {agent}")

print("\nPlanner Reason:")
print(plan["reason"])

print("\n===== TEST PASSED =====")