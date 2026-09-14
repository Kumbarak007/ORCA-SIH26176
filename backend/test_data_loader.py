from data_loader import (
    load_pfz_data,
    load_ocean_data,
    load_weather_data,
    load_gis_data
)


print("\n===== ORCA DATA LOADER TEST =====\n")


pfz = load_pfz_data()
ocean = load_ocean_data()
weather = load_weather_data()
gis = load_gis_data()


print("PFZ zones:", len(pfz))
print("Ocean records:", len(ocean))
print("Weather records:", len(weather))
print("GIS records:", len(gis))


print("\n===== SAMPLE DATA =====\n")

print("PFZ:")
print(pfz[0])

print("\nOcean:")
print(ocean[0])

print("\nWeather:")
print(weather[0])

print("\nGIS:")
print(gis[0])


print("\n===== TEST PASSED =====")