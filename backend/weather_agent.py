from data_loader import load_weather_data


class WeatherAgent:
    """
    ORCA Weather Intelligence Agent.

    Retrieves weather conditions and risk information
    for each candidate fishing zone.
    """

    def __init__(self):
        self.name = "Weather Agent"

    def get_weather_conditions(self):
        """
        Load and return weather conditions for all zones.
        """

        weather_data = load_weather_data()

        conditions = []

        for zone in weather_data:
            conditions.append({
                "zone_id": zone["zone_id"],
                "wind_speed": zone["wind_speed"],
                "rainfall": zone["rainfall"],
                "storm": zone["storm"],
                "visibility": zone["visibility"],
                "risk": zone["risk"],
                "timestamp": zone["timestamp"]
            })

        return conditions