from gis_agent import GISAgent


agent = GISAgent()
spatial_info = agent.get_spatial_information()

print("\n===== ORCA GIS AGENT TEST =====\n")

print("Agent:", agent.name)
print("Number of zones:", len(spatial_info))

print("\nSpatial Information:\n")

for zone in spatial_info:
    print(
        f"{zone['zone_id']} | "
        f"Distance: {zone['distance_km']} km | "
        f"Restricted: {zone['restricted']}"
    )

print("\n===== TEST PASSED =====")