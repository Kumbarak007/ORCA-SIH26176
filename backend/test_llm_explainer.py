from evidence_fusion import EvidenceFusion
from candidate_plan_engine import CandidatePlanEngine
from recommendation_engine import RecommendationEngine
from llm_explainer import LLMExplainer


# 1. Collect fused evidence
fusion = EvidenceFusion()
fused_data = fusion.fuse_zone_evidence()


# 2. Generate candidate plans
candidate_engine = CandidatePlanEngine()
plans = candidate_engine.generate_plans(fused_data)


# 3. Generate deterministic recommendation
recommendation_engine = RecommendationEngine()

recommendation = recommendation_engine.generate_recommendation(
    plans,
    fused_data
)


# 4. Generate natural-language explanation
explainer = LLMExplainer()

explanation = explainer.explain_recommendation(
    recommendation,
    recommendation.evidence
)


print("\n===== ORCA LLM EXPLAINER TEST =====\n")

print("Explainer:", explainer.name)

print("\nVERIFIED RECOMMENDATION")
print("-----------------------")
print("Recommended Zone:", recommendation.zone_id)
print("Score:", recommendation.score)
print("Status:", recommendation.status)

print("\nLLM EXPLANATION")
print("----------------")
print(explanation)

print("\n===== TEST PASSED =====")