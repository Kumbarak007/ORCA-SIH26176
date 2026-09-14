from data_loader import load_pfz_data


class PFZAgent:
    """
    ORCA Potential Fishing Zone Agent.

    Retrieves PFZ information from the prototype
    PFZ dataset and returns candidate fishing zones.
    """

    def __init__(self):
        self.name = "PFZ Agent"

    def get_fishing_zones(self):
        """
        Load and return all available PFZ zones.
        """

        pfz_data = load_pfz_data()

        zones = []

        for zone in pfz_data:
            zones.append({
                "zone_id": zone["zone_id"],
                "latitude": zone["latitude"],
                "longitude": zone["longitude"],
                "suitability": zone["suitability"],
                "confidence": zone["confidence"],
                "valid_time": zone["valid_time"]
            })

        return zones