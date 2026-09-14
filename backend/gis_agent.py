from data_loader import load_gis_data


class GISAgent:
    """
    ORCA GIS Intelligence Agent.

    Retrieves spatial information such as distance
    and restricted-area status for each zone.
    """

    def __init__(self):
        self.name = "GIS Agent"

    def get_spatial_information(self):
        """
        Load and return GIS information for all zones.
        """

        gis_data = load_gis_data()

        spatial_info = []

        for zone in gis_data:
            spatial_info.append({
                "zone_id": zone["zone_id"],
                "distance_km": zone["distance_from_start_km"],
                "restricted": zone["restricted"]
            })

        return spatial_info