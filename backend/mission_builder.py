from schemas import (
    Mission,
    MissionConstraints,
    MissionPreferences
)


class MissionBuilder:
    """
    ORCA Mission Builder.

    Converts the structured output from the Mission Parser
    into an ORCA Mission object.
    """

    def __init__(self):
        self.name = "Mission Builder"

    def build_mission(self, parsed_data):
        """
        Convert parsed mission data into an ORCA Mission.
        """

        constraints = MissionConstraints(
    avoid_high_wind=parsed_data.get(
        "avoid_high_wind",
        True
    ),
    avoid_unsafe_sea=parsed_data.get(
        "avoid_unsafe_sea",
        True
    ),
    avoid_restricted_areas=parsed_data.get(
        "avoid_restricted_areas",
        True
    ),
    max_wave_height=parsed_data.get(
        "max_wave_height"
    )
)

        preferences = MissionPreferences(
    maximize_fishing_potential=parsed_data.get(
        "maximize_fishing_potential",
        True
    ),
    minimize_risk=parsed_data.get(
        "minimize_risk",
        True
    ),
    minimize_travel_distance=parsed_data.get(
        "minimize_travel_distance",
        True
    ),
    primary_preference=parsed_data.get(
        "primary_preference",
        "balanced"
    )
)

        mission = Mission(
            objective=parsed_data.get(
                "objective", ""
            ),

            location=parsed_data.get(
                "location", ""
            ),

            departure_time=parsed_data.get(
                "departure_time", ""
            ),

            fishing_duration_hours=parsed_data.get(
                "fishing_duration_hours"
            ),

            return_deadline=parsed_data.get(
                "return_deadline", ""
            ),

            constraints=constraints,

            preferences=preferences
        )

        return mission