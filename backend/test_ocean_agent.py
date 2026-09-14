from ocean_agent import OceanAgent


agent = OceanAgent()
conditions = agent.get_ocean_conditions()

print("\n===== ORCA OCEAN AGENT TEST =====\n")

print("Agent:", agent.name)
print("Number of zones:", len(conditions))

print("\nOcean Conditions:\n")

for zone in conditions:
    print(
        f"{zone['zone_id']} | "
        f"Chlorophyll-a: {zone['chlorophyll_a']} mg/m³ | "
        f"SST: {zone['sst']} °C | "
        f"Wave: {zone['wave_height']} m | "
        f"Current: {zone['current_speed']} m/s"
    )

print("\n===== TEST PASSED =====")