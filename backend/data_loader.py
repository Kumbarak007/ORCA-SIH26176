import json
from pathlib import Path


# Find the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directory
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    """
    Load a JSON file from the ORCA data directory.
    """

    file_path = DATA_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_pfz_data():
    return load_json("pfz.json")


def load_ocean_data():
    return load_json("ocean.json")


def load_weather_data():
    return load_json("weather.json")


def load_gis_data():
    return load_json("gis.json")