from schemas import Recommendation, Evidence, CandidatePlan


class RecommendationEngine:
    """
    ORCA Mission Recommendation Engine.

    Selects the best feasible candidate plan and
    preserves the evidence and rejected alternatives
    behind the decision.
    """

    def __init__(self):
        self.name = "Recommendation Engine"

    def build_evidence_chain(self, zone):
        """
        Build a structured evidence chain from fused zone data.
        """

        evidence = [
            Evidence(
                source="PFZ Agent",
                zone_id=zone["zone_id"],
                variable="Fishing suitability",
                value=zone["pfz"]["suitability"],
                confidence=zone["pfz"]["confidence"],
                timestamp=zone["pfz"]["valid_time"]
            ),

            Evidence(
                source="Ocean Agent",
                zone_id=zone["zone_id"],
                variable="Chlorophyll-a",
                value=zone["ocean"]["chlorophyll_a"],
                unit="mg/m³",
                confidence=zone["ocean"]["confidence"],
                timestamp=zone["ocean"]["timestamp"]
            ),

            Evidence(
                source="Ocean Agent",
                zone_id=zone["zone_id"],
                variable="Sea Surface Temperature",
                value=zone["ocean"]["sst"],
                unit="°C",
                confidence=zone["ocean"]["confidence"],
                timestamp=zone["ocean"]["timestamp"]
            ),

            Evidence(
                source="Ocean Agent",
                zone_id=zone["zone_id"],
                variable="Wave height",
                value=zone["ocean"]["wave_height"],
                unit="m",
                confidence=zone["ocean"]["confidence"],
                timestamp=zone["ocean"]["timestamp"]
            ),

            Evidence(
                source="Ocean Agent",
                zone_id=zone["zone_id"],
                variable="Current speed",
                value=zone["ocean"]["current_speed"],
                unit="m/s",
                confidence=zone["ocean"]["confidence"],
                timestamp=zone["ocean"]["timestamp"]
            ),

            Evidence(
                source="Weather Agent",
                zone_id=zone["zone_id"],
                variable="Wind speed",
                value=zone["weather"]["wind_speed"],
                unit="km/h",
                confidence=1.0,
                timestamp=zone["weather"]["timestamp"]
            ),

            Evidence(
                source="Weather Agent",
                zone_id=zone["zone_id"],
                variable="Weather risk",
                value=zone["weather"]["risk"],
                confidence=1.0,
                timestamp=zone["weather"]["timestamp"]
            ),

            Evidence(
                source="GIS Agent",
                zone_id=zone["zone_id"],
                variable="Distance from start",
                value=zone["gis"]["distance_km"],
                unit="km",
                confidence=1.0
            ),

            Evidence(
                source="GIS Agent",
                zone_id=zone["zone_id"],
                variable="Restricted area",
                value=zone["gis"]["restricted"],
                confidence=1.0
            )
        ]

        return evidence

    def generate_recommendation(self, plans, fused_data):
        """
        Select the highest-scoring feasible plan
        and attach its evidence chain.
        """

        feasible_plans = [
            plan for plan in plans
            if plan["feasible"]
        ]

        rejected_plans = [
            plan for plan in plans
            if not plan["feasible"]
        ]

        # No feasible plan available
        if not feasible_plans:
            return Recommendation(
                selected_plan_id=None,
                zone_id=None,
                score=0,
                status="NO_FEASIBLE_PLAN",
                rationale=(
                    "No candidate zone satisfies all hard constraints."
                ),
                evidence=[],
                rejected_plans=[
                    CandidatePlan(
                        plan_id=plan["plan_id"],
                        zone_id=plan["zone_id"],
                        score=plan["score"],
                        feasible=plan["feasible"],
                        rejection_reasons=plan["rejection_reasons"]
                    )
                    for plan in rejected_plans
                ]
            )

        # Select highest-scoring feasible plan
        selected_plan = max(
            feasible_plans,
            key=lambda plan: plan["score"]
        )

        # Find complete fused evidence for selected zone
        selected_zone = next(
            zone for zone in fused_data
            if zone["zone_id"] == selected_plan["zone_id"]
        )

        evidence_chain = self.build_evidence_chain(selected_zone)

        # Convert rejected plans into CandidatePlan objects
        rejected_plan_objects = [
            CandidatePlan(
                plan_id=plan["plan_id"],
                zone_id=plan["zone_id"],
                score=plan["score"],
                feasible=plan["feasible"],
                rejection_reasons=plan["rejection_reasons"]
            )
            for plan in rejected_plans
        ]

        rationale = (
            f"{selected_plan['zone_id']} was selected because it is "
            f"feasible and has the highest score of "
            f"{selected_plan['score']} among feasible candidate plans."
        )

        return Recommendation(
            selected_plan_id=selected_plan["plan_id"],
            zone_id=selected_plan["zone_id"],
            score=selected_plan["score"],
            status="FEASIBLE",
            rationale=rationale,
            evidence=evidence_chain,
            rejected_plans=rejected_plan_objects
        )