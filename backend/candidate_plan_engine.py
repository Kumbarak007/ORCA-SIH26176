from decision_engine import DecisionEngine


class CandidatePlanEngine:
    """
    ORCA Candidate Plan Engine.

    Evaluates all fused zones and creates candidate
    plans based on feasibility and score.
    """

    def __init__(self):
        self.name = "Candidate Plan Engine"
        self.decision_engine = DecisionEngine()

    def generate_plans(
    self,
    fused_data,
    constraints=None,
    preferences=None
    ):
        """
        Generate candidate plans for all available zones.
        """

        plans = []

        for zone in fused_data:

            result = self.decision_engine.evaluate_zone(
            zone,
            constraints,
            preferences
            )

            plan = {
                "plan_id": f"PLAN_{zone['zone_id']}",
                "zone_id": zone["zone_id"],
                "feasible": result["feasible"],
                "score": result["score"],
                "rejection_reasons": result["rejection_reasons"]
            }

            plans.append(plan)

        # Rank feasible plans by score
        feasible_plans = [
            plan for plan in plans
            if plan["feasible"]
        ]

        rejected_plans = [
            plan for plan in plans
            if not plan["feasible"]
        ]

        feasible_plans.sort(
            key=lambda plan: plan["score"],
            reverse=True
        )

        return feasible_plans + rejected_plans