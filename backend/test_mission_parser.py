from mission_parser import MissionParser


parser = MissionParser()

user_mission = (
    "I want to go fishing near Goa tomorrow morning "
    "for 5 hours. Avoid high wind and restricted areas."
)

result = parser.parse_mission(user_mission)


print("\n===== ORCA MISSION PARSER TEST =====\n")

print("Parser:", parser.name)

print("\nUser Mission:")
print(user_mission)

print("\nParsed Mission:")
print(result)

print("\n===== TEST PASSED =====")