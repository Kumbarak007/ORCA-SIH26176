from pfz_agent import PFZAgent
from ocean_agent import OceanAgent
from weather_agent import WeatherAgent
from gis_agent import GISAgent


class EvidenceFusion:
    """
    ORCA Evidence Fusion Layer.

    Combines evidence from PFZ, Ocean, Weather,
    and GIS agents for each candidate zone.
    """

    def __init__(self):
        self.pfz_agent = PFZAgent()
        self.ocean_agent = OceanAgent()
        self.weather_agent = WeatherAgent()
        self.gis_agent = GISAgent()

    def fuse_zone_evidence(self):
        """
        Combine information from all four agents
        zone by zone.
        """

        pfz_data = self.pfz_agent.get_fishing_zones()
        ocean_data = self.ocean_agent.get_ocean_conditions()
        weather_data = self.weather_agent.get_weather_conditions()
        gis_data = self.gis_agent.get_spatial_information()

        fused_data = []

        for pfz in pfz_data:

            zone_id = pfz["zone_id"]

            ocean = next(
                item for item in ocean_data
                if item["zone_id"] == zone_id
            )

            weather = next(
                item for item in weather_data
                if item["zone_id"] == zone_id
            )

            gis = next(
                item for item in gis_data
                if item["zone_id"] == zone_id
            )

            fused_zone = {
                "zone_id": zone_id,

                "location": {
                    "latitude": pfz["latitude"],
                    "longitude": pfz["longitude"]
                },

                "pfz": {
                    "suitability": pfz["suitability"],
                    "confidence": pfz["confidence"],
                    "valid_time": pfz["valid_time"]
                },

                "ocean": {
                    "chlorophyll_a": ocean["chlorophyll_a"],
                    "sst": ocean["sst"],
                    "wave_height": ocean["wave_height"],
                    "current_speed": ocean["current_speed"],
                    "confidence": ocean["confidence"],
                    "timestamp": ocean["timestamp"]
                },

                "weather": {
                    "wind_speed": weather["wind_speed"],
                    "rainfall": weather["rainfall"],
                    "storm": weather["storm"],
                    "visibility": weather["visibility"],
                    "risk": weather["risk"],
                    "timestamp": weather["timestamp"]
                },

                "gis": {
                    "distance_km": gis["distance_km"],
                    "restricted": gis["restricted"]
                }
            }

            fused_data.append(fused_zone)

        return fused_data