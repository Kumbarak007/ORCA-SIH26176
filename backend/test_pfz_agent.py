from pfz_agent import PFZAgent


agent = PFZAgent()

zones = agent.get_fishing_zones()


print("\n===== ORCA PFZ AGENT TEST =====\n")

print("Agent:", agent.name)

print("Number of candidate zones:", len(zones))

print("\nCandidate Fishing Zones:\n")

for zone in zones:
    print(
        f"{zone['zone_id']} | "
        f"Suitability: {zone['suitability']} | "
        f"Confidence: {zone['confidence']}"
    )

print("\n===== TEST PASSED =====")