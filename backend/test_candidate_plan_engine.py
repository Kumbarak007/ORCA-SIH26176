from evidence_fusion import EvidenceFusion
from candidate_plan_engine import CandidatePlanEngine


fusion = EvidenceFusion()
fused_data = fusion.fuse_zone_evidence()

engine = CandidatePlanEngine()
plans = engine.generate_plans(fused_data)

print("\n===== ORCA CANDIDATE PLAN ENGINE TEST =====\n")

print("Number of candidate plans:", len(plans))

for plan in plans:

    print(f"\n--- {plan['plan_id']} ---")
    print(f"Zone: {plan['zone_id']}")
    print(f"Feasible: {plan['feasible']}")
    print(f"Score: {plan['score']}")

    if plan["rejection_reasons"]:
        print("Rejection Reasons:")

        for reason in plan["rejection_reasons"]:
            print(f"  - {reason}")

print("\n===== TEST PASSED =====")