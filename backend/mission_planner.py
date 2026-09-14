class MissionPlanner:
    """
    ORCA Mission Planner.

    Determines which domain agents are required for a marine
    mission. Agent selection is deterministic because ORCA
    always requires PFZ, Ocean, Weather, and GIS evidence.
    """

    def __init__(self):
        self.name = "Mission Planner"

        self.required_agents = [
            "PFZ",
            "Ocean",
            "Weather",
            "GIS"
        ]

    def plan(self, mission):
        """
        Select all required ORCA domain agents.

        The planner does not make the final recommendation,
        calculate scores, or override safety constraints.
        """

        return {
            "selected_agents": self.required_agents.copy(),
            "reason": (
                "PFZ, Ocean, Weather, and GIS agents are required "
                "to evaluate fishing potential, ocean conditions, "
                "weather safety, and spatial constraints."
            )
        }