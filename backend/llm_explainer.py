class LLMExplainer:
    """
    ORCA Evidence Explanation Engine.

    Generates a concise explanation directly from the
    verified recommendation and evidence. It does not
    call an external LLM, recalculate scores, or modify
    the recommendation.
    """

    def __init__(self):
        self.name = "Evidence Explanation Engine"

    def explain_recommendation(self, recommendation, evidence):
        if recommendation.status == "NO_FEASIBLE_PLAN":
            explanation = (
                "No feasible fishing zone was found because all "
                "candidate zones violated one or more safety or "
                "spatial constraints."
            )

            if recommendation.rejected_plans:
                explanation += "\n\nRejected alternatives:"

                for plan in recommendation.rejected_plans:
                    explanation += (
                        f"\n- {plan.zone_id}: "
                        f"{'; '.join(plan.rejection_reasons)}"
                    )

            return explanation

        zone_id = recommendation.zone_id

        evidence_map = {
            item.variable: item.value
            for item in evidence
        }

        suitability = evidence_map.get(
            "Fishing suitability",
            "N/A"
        )

        chlorophyll = evidence_map.get(
            "Chlorophyll-a",
            "N/A"
        )

        sst = evidence_map.get(
            "Sea Surface Temperature",
            "N/A"
        )

        wave_height = evidence_map.get(
            "Wave height",
            "N/A"
        )

        current_speed = evidence_map.get(
            "Current speed",
            "N/A"
        )

        wind_speed = evidence_map.get(
            "Wind speed",
            "N/A"
        )

        weather_risk = evidence_map.get(
            "Weather risk",
            "N/A"
        )

        distance = evidence_map.get(
            "Distance from start",
            "N/A"
        )

        explanation = (
            f"{zone_id} is the recommended fishing zone with "
            f"a decision score of {recommendation.score}. "
            f"The zone is feasible under the configured safety "
            f"and spatial constraints.\n\n"
            
            f"Fishing suitability: {suitability}.\n"
            f"Chlorophyll-a: {chlorophyll} mg/m³.\n"
            f"Sea surface temperature: {sst} °C.\n"
            f"Wave height: {wave_height} m.\n"
            f"Current speed: {current_speed} m/s.\n"
            f"Wind speed: {wind_speed} km/h.\n"
            f"Weather risk: {weather_risk}.\n"
            f"Distance from start: {distance} km.\n\n"
            
            "The recommendation is based on the fused evidence "
            "from the PFZ, Ocean, Weather, and GIS agents. "
            "Chlorophyll-a is presented as an oceanographic "
            "indicator and is not treated as a direct fish-catch "
            "prediction."
        )

        if recommendation.rejected_plans:
            explanation += "\n\nRejected alternatives:"

            for plan in recommendation.rejected_plans:
                explanation += (
                    f"\n- {plan.zone_id}: "
                    f"{'; '.join(plan.rejection_reasons)}"
                )

        return explanation