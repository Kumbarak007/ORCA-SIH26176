from evidence_fusion import EvidenceFusion
from candidate_plan_engine import CandidatePlanEngine
from recommendation_engine import RecommendationEngine


fusion = EvidenceFusion()
fused_data = fusion.fuse_zone_evidence()

candidate_engine = CandidatePlanEngine()
plans = candidate_engine.generate_plans(fused_data)

recommendation_engine = RecommendationEngine()

recommendation = recommendation_engine.generate_recommendation(
    plans,
    fused_data
)


print("\n===== ORCA RECOMMENDATION ENGINE TEST =====\n")

print("Engine:", recommendation_engine.name)

print("\nFINAL RECOMMENDATION")
print("-------------------")

print("Selected Plan:", recommendation.selected_plan_id)
print("Recommended Zone:", recommendation.zone_id)
print("Score:", recommendation.score)
print("Status:", recommendation.status)
print("Rationale:", recommendation.rationale)


print("\nMISSION DECISION EVIDENCE CHAIN")
print("--------------------------------")

for evidence in recommendation.evidence:
    unit = f" {evidence.unit}" if evidence.unit else ""

    print(
        f"{evidence.source} | "
        f"{evidence.variable} | "
        f"Value: {evidence.value}{unit} | "
        f"Confidence: {evidence.confidence}"
    )


print("\nREJECTED ALTERNATIVES")
print("---------------------")

for plan in recommendation.rejected_plans:

    print(f"\n{plan.plan_id}")

    for reason in plan.rejection_reasons:
        print(f"  - {reason}")


print("\n===== TEST PASSED =====")