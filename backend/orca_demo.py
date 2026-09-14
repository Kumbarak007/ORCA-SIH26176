from mission_orchestrator import MissionOrchestrator
from llm_explainer import LLMExplainer


def main():

    print("\n========================================")
    print("        ORCA MARINE INTELLIGENCE")
    print("========================================")

    print("\nDescribe your marine mission.")
    print("You can continue with follow-up requests.")
    print("Type 'exit' to stop.")

    orchestrator = MissionOrchestrator()
    explainer = LLMExplainer()

    # Stores the conversation between the user and ORCA
    conversation_history = []

    while True:

        user_input = input("\nMission / Follow-up: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            print("Please enter a mission or follow-up request.")
            continue

        # Store user message
        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        try:

            # Run ORCA with conversation history
            result = orchestrator.run_mission(
                user_input,
                conversation_history
            )

            mission = result["mission"]
            planner_result = result["planner_result"]
            recommendation = result["recommendation"]

            explanation = explainer.explain_recommendation(
                recommendation,
                recommendation.evidence
            )

            # ----------------------------------------
            # DISPLAY MISSION
            # ----------------------------------------

            print("\n\n========== MISSION ==========")

            print("Objective:", mission.objective)
            print("Location:", mission.location)
            print("Departure:", mission.departure_time)
            print(
                "Fishing Duration:",
                mission.fishing_duration_hours,
                "hours"
            )

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

            print(
                "Primary Preference:",
                mission.preferences.primary_preference
            )

            if mission.constraints.max_wave_height is not None:
                print(
                    "Maximum Wave Height:",
                    mission.constraints.max_wave_height,
                    "m"
                )

            # ----------------------------------------
            # DISPLAY PLANNER
            # ----------------------------------------

            print("\n\n========== AGENTS USED ==========")

            for agent in planner_result["selected_agents"]:
                print("✓", agent)

            print("\nPlanner Reason:")
            print(planner_result["reason"])

            # ----------------------------------------
            # DISPLAY RECOMMENDATION
            # ----------------------------------------

            print("\n\n========== FINAL RECOMMENDATION ==========")

            print("Recommended Zone:", recommendation.zone_id)
            print("Selected Plan:", recommendation.selected_plan_id)
            print("Score:", recommendation.score)
            print("Status:", recommendation.status)

            # ----------------------------------------
            # DISPLAY EVIDENCE
            # ----------------------------------------

            print("\n\n========== DECISION EVIDENCE ==========")

            for evidence in recommendation.evidence:

                unit = (
                    f" {evidence.unit}"
                    if evidence.unit
                    else ""
                )

                print(
                    f"{evidence.source} | "
                    f"{evidence.variable} | "
                    f"{evidence.value}{unit} | "
                    f"Confidence: {evidence.confidence}"
                )

            # ----------------------------------------
            # DISPLAY REJECTED ALTERNATIVES
            # ----------------------------------------

            print("\n\n========== REJECTED ALTERNATIVES ==========")

            for plan in recommendation.rejected_plans:

                print(f"\n{plan.plan_id}")

                for reason in plan.rejection_reasons:
                    print("  -", reason)

            # ----------------------------------------
            # DISPLAY EXPLANATION
            # ----------------------------------------

            print("\n\n========== AI EXPLANATION ==========")

            print(explanation)

            # Store ORCA response context
            conversation_history.append({
                "role": "assistant",
                "content": explanation
            })

            print("\n========================================")
            print("      ORCA IS READY FOR FOLLOW-UP")
            print("========================================")

        except Exception as e:

            print("\n========== ORCA ERROR ==========")
            print(e)
            print("================================")

    print("\n========================================")
    print("          ORCA DEMO COMPLETE")
    print("========================================\n")


if __name__ == "__main__":
    main()