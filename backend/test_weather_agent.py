from weather_agent import WeatherAgent


agent = WeatherAgent()
conditions = agent.get_weather_conditions()

print("\n===== ORCA WEATHER AGENT TEST =====\n")

print("Agent:", agent.name)
print("Number of zones:", len(conditions))

print("\nWeather Conditions:\n")

for zone in conditions:
    print(
        f"{zone['zone_id']} | "
        f"Wind: {zone['wind_speed']} km/h | "
        f"Rainfall: {zone['rainfall']} mm | "
        f"Storm: {zone['storm']} | "
        f"Visibility: {zone['visibility']} km | "
        f"Risk: {zone['risk']}"
    )

print("\n===== TEST PASSED =====")