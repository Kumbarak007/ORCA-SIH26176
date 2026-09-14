from evidence_fusion import EvidenceFusion


fusion = EvidenceFusion()
fused_data = fusion.fuse_zone_evidence()

print("\n===== ORCA EVIDENCE FUSION TEST =====\n")

print("Number of fused zones:", len(fused_data))

for zone in fused_data:
    print(f"\n--- {zone['zone_id']} ---")

    print(
        f"PFZ Suitability: {zone['pfz']['suitability']} | "
        f"Confidence: {zone['pfz']['confidence']}"
    )

    print(
        f"Chlorophyll-a: {zone['ocean']['chlorophyll_a']} mg/m³ | "
        f"SST: {zone['ocean']['sst']} °C | "
        f"Wave: {zone['ocean']['wave_height']} m | "
        f"Current: {zone['ocean']['current_speed']} m/s"
    )

    print(
        f"Weather Risk: {zone['weather']['risk']} | "
        f"Wind: {zone['weather']['wind_speed']} km/h"
    )

    print(
        f"Distance: {zone['gis']['distance_km']} km | "
        f"Restricted: {zone['gis']['restricted']}"
    )

print("\n===== TEST PASSED =====")