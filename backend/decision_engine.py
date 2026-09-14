# class DecisionEngine:
#     """
#     ORCA Deterministic Decision Engine.

#     Applies hard constraints first and then calculates
#     a score for feasible fishing zones.
#     """

#     def __init__(self):
#         self.name = "Decision Engine"

#         # Hard safety constraints
#         self.max_wind_speed = 20
#         self.max_wave_height = 1.5

#     def evaluate_zone(self, zone, constraints=None):
#         """
#         Evaluate one zone using deterministic rules.
#         """

#         rejection_reasons = []

#         weather = zone["weather"]
#         ocean = zone["ocean"]
#         gis = zone["gis"]
#         pfz = zone["pfz"]

#         # -----------------------------
#         # HARD CONSTRAINTS
#         # -----------------------------

#         if weather["risk"] == "HIGH":
#             rejection_reasons.append(
#                 "High weather risk"
#             )

#         if weather["wind_speed"] > self.max_wind_speed:
#             rejection_reasons.append(
#                 f"Wind speed exceeds {self.max_wind_speed} km/h"
#             )

#         if ocean["wave_height"] > self.max_wave_height:
#             rejection_reasons.append(
#                 f"Wave height exceeds {self.max_wave_height} m"
#             )
#             if (
#                 constraints is not None
#                 and constraints.max_wave_height is not None
#                 and zone["ocean"]["wave_height"] > constraints.max_wave_height
#                 ):
#                 rejection_reasons.append(
#                     f"Wave height exceeds user limit of "
#                     f"{constraints.max_wave_height} m"
#                 )

#         if weather["storm"]:
#             rejection_reasons.append(
#                 "Storm conditions detected"
#             )

#         if gis["restricted"]:
#             rejection_reasons.append(
#                 "Zone is inside a restricted area"
#             )

#         # -----------------------------
#         # FEASIBILITY
#         # -----------------------------

#         feasible = len(rejection_reasons) == 0

#         # -----------------------------
#         # SCORING
#         # -----------------------------

#         if feasible:

#             fishing_potential = pfz["suitability"]

#             safety_score = 1 - min(
#                 weather["wind_speed"] / 40,
#                 1
#             )

#             distance_score = 1 - min(
#                 gis["distance_km"] / 50,
#                 1
#             )

#             ocean_score = (
#                 0.4 * fishing_potential
#                 + 0.3 * safety_score
#                 + 0.3 * distance_score
#             )

#             score = round(ocean_score * 100, 2)

#         else:
#             score = 0

#         return {
#             "zone_id": zone["zone_id"],
#             "feasible": feasible,
#             "score": score,
#             "rejection_reasons": rejection_reasons
#         }

class DecisionEngine:
    """
    ORCA Deterministic Decision Engine.

    Applies hard constraints first and then calculates
    a score for feasible fishing zones based on the
    user's primary mission preference.
    """

    def __init__(self):
        self.name = "Decision Engine"

        # Default hard safety constraints
        self.max_wind_speed = 20
        self.max_wave_height = 1.5

    def evaluate_zone(
        self,
        zone,
        constraints=None,
        preferences=None
    ):
        """
        Evaluate one zone using deterministic rules.
        """

        rejection_reasons = []

        weather = zone["weather"]
        ocean = zone["ocean"]
        gis = zone["gis"]
        pfz = zone["pfz"]

        # -----------------------------
        # HARD SAFETY CONSTRAINTS
        # -----------------------------

        if weather["risk"] == "HIGH":
            rejection_reasons.append(
                "High weather risk"
            )

        if weather["wind_speed"] > self.max_wind_speed:
            rejection_reasons.append(
                f"Wind speed exceeds "
                f"{self.max_wind_speed} km/h"
            )

        # Default safety wave limit
        if ocean["wave_height"] > self.max_wave_height:
            rejection_reasons.append(
                f"Wave height exceeds "
                f"{self.max_wave_height} m"
            )

        # User-specific wave constraint
        if (
            constraints is not None
            and constraints.max_wave_height is not None
            and ocean["wave_height"] >
                constraints.max_wave_height
        ):
            rejection_reasons.append(
                f"Wave height exceeds user limit of "
                f"{constraints.max_wave_height} m"
            )

        if weather["storm"]:
            rejection_reasons.append(
                "Storm conditions detected"
            )

        if gis["restricted"]:
            rejection_reasons.append(
                "Zone is inside a restricted area"
            )

        # -----------------------------
        # FEASIBILITY
        # -----------------------------

        feasible = len(rejection_reasons) == 0

        # -----------------------------
        # SCORING
        # -----------------------------

        if feasible:

            # Fishing potential score
            fishing_potential = pfz["suitability"]

            # Safety score
            safety_score = 1 - min(
                weather["wind_speed"] / 40,
                1
            )

            # Distance score
            distance_score = 1 - min(
                gis["distance_km"] / 50,
                1
            )

            # ----------------------------------------
            # DETERMINE USER'S PRIMARY PREFERENCE
            # ----------------------------------------

            primary_preference = "balanced"

            if preferences is not None:
                primary_preference = (
                    preferences.primary_preference
                )

            # ----------------------------------------
            # DYNAMIC WEIGHTS
            # ----------------------------------------

            if primary_preference == "fishing_potential":
                fishing_weight = 0.70
                safety_weight = 0.20
                distance_weight = 0.10

            elif primary_preference == "safety":
                fishing_weight = 0.20
                safety_weight = 0.70
                distance_weight = 0.10
                
            elif primary_preference == "distance":
                fishing_weight = 0.20
                safety_weight = 0.10
                distance_weight = 0.70

            else:

                # Balanced mission
                fishing_weight = 0.40
                safety_weight = 0.30
                distance_weight = 0.30

            # ----------------------------------------
            # FINAL SCORE
            # ----------------------------------------

            ocean_score = (
                fishing_weight * fishing_potential
                + safety_weight * safety_score
                + distance_weight * distance_score
            )

            score = round(
                ocean_score * 100,
                2
            )

        else:

            score = 0

        # -----------------------------
        # RETURN RESULT
        # -----------------------------

        return {
            "zone_id": zone["zone_id"],
            "feasible": feasible,
            "score": score,
            "rejection_reasons": rejection_reasons
        }