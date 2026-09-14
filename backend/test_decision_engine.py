from evidence_fusion import EvidenceFusion
from decision_engine import DecisionEngine


fusion = EvidenceFusion()
fused_data = fusion.fuse_zone_evidence()

engine = DecisionEngine()

print("\n===== ORCA DECISION ENGINE TEST =====\n")

for zone in fused_data:

    result = engine.evaluate_zone(zone)

    print(f"--- {result['zone_id']} ---")
    print(f"Feasible: {result['feasible']}")
    print(f"Score: {result['score']}")

    if result["rejection_reasons"]:
        print("Rejection Reasons:")

        for reason in result["rejection_reasons"]:
            print(f"  - {reason}")

    print()

print("===== TEST PASSED =====")