from mission_orchestrator import MissionOrchestrator


orchestrator = MissionOrchestrator()

user_mission = (
    "I want to go fishing near Goa tomorrow morning "
    "for 5 hours. Avoid high wind and restricted areas."
)

result = orchestrator.run_mission(user_mission)

mission = result["mission"]
recommendation = result["recommendation"]


print("\n===== ORCA MISSION ORCHESTRATOR TEST =====\n")

print("Orchestrator:", orchestrator.name)

print("\nMISSION")
print("-------")
print("Objective:", mission.objective)
print("Location:", mission.location)
print("Departure:", mission.departure_time)
print("Fishing Duration:", mission.fishing_duration_hours)

print("\nRECOMMENDATION")
print("--------------")
print("Selected Plan:", recommendation.selected_plan_id)
print("Recommended Zone:", recommendation.zone_id)
print("Score:", recommendation.score)
print("Status:", recommendation.status)
print("Rationale:", recommendation.rationale)

print("\nEVIDENCE COUNT")
print("--------------")
print("Evidence items:", len(recommendation.evidence))

print("\nREJECTED ALTERNATIVES")
print("---------------------")

for plan in recommendation.rejected_plans:
    print(plan.plan_id)

    for reason in plan.rejection_reasons:
        print(f"  - {reason}")

print("\n===== TEST PASSED =====")