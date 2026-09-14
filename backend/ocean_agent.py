from data_loader import load_ocean_data


class OceanAgent:
    """
    ORCA Ocean Intelligence Agent.

    Retrieves ocean conditions including Chlorophyll-a,
    SST, wave height, and current speed.
    """

    def __init__(self):
        self.name = "Ocean Agent"

    def get_ocean_conditions(self):
        """
        Load and return ocean conditions for all zones.
        """

        ocean_data = load_ocean_data()

        conditions = []

        for zone in ocean_data:
            conditions.append({
                "zone_id": zone["zone_id"],
                "chlorophyll_a": zone["chlorophyll_a"],
                "sst": zone["sst"],
                "wave_height": zone["wave_height"],
                "current_speed": zone["current_speed"],
                "confidence": zone["confidence"],
                "timestamp": zone["timestamp"]
            })

        return conditions