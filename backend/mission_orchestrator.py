from mission_parser import MissionParser
from mission_builder import MissionBuilder
from mission_planner import MissionPlanner
from evidence_fusion import EvidenceFusion
from candidate_plan_engine import CandidatePlanEngine
from recommendation_engine import RecommendationEngine


class MissionOrchestrator:
    """
    ORCA Mission Orchestrator.

    Coordinates the complete mission planning workflow
    from natural-language input to a final recommendation.
    """

    def __init__(self):
        self.name = "Mission Orchestrator"

        self.mission_parser = MissionParser()
        self.mission_builder = MissionBuilder()
        self.mission_planner = MissionPlanner()
        self.evidence_fusion = EvidenceFusion()
        self.candidate_plan_engine = CandidatePlanEngine()
        self.recommendation_engine = RecommendationEngine()

    # def run_mission(self, user_input):
    def run_mission(self, user_input, conversation_history=None):
        """
        Execute the complete ORCA mission workflow.
        """

        # 1. Parse natural-language mission using LLM
        # parsed_data = self.mission_parser.parse_mission(
        #     user_input
        # )

        parsed_data = self.mission_parser.parse_mission(
            user_input,
            conversation_history
            )

        # Reject unrelated non-marine messages
        if not parsed_data.get("is_marine_mission", True):
            raise ValueError(
                "This does not appear to be a marine mission. "
                "Please describe a marine or fishing mission "
                "you want ORCA to analyze."
            )

        # 2. Convert parsed data into ORCA Mission object
        mission = self.mission_builder.build_mission(
            parsed_data
        )

        # 3. Use LLM planner to determine relevant domain agents
        planner_result = self.mission_planner.plan(
            mission
        )

        # 4. Collect and combine evidence
        fused_data = self.evidence_fusion.fuse_zone_evidence()

        # 5. Generate candidate plans
        plans = self.candidate_plan_engine.generate_plans(
            fused_data,
            mission.constraints,
            mission.preferences
        )

        # 6. Generate final deterministic recommendation
        recommendation = (
            self.recommendation_engine.generate_recommendation(
                plans,
                fused_data
            )
        )

        return {
            "mission": mission,
            "parsed_data": parsed_data,
            "planner_result": planner_result,
            "fused_data": fused_data,
            "plans": plans,
            "recommendation": recommendation
        }