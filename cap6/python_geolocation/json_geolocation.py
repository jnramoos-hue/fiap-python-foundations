import json
import os
from geopy.geocoders import Nominatim

input_file = "addresses.json"
output_file = "geocoded_addresses.json"

if os.path.exists(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        addresses = json.load(file)

    geolocator = Nominatim(user_agent="fiap_python_foundations")
    results = []

    for item in addresses:
        location = geolocator.geocode(item["address"])

        if location is not None:
            results.append({
                "address": location.address,
                "latitude": location.latitude,
                "longitude": location.longitude
            })
        else:
            results.append({
                "address": item["address"],
                "latitude": None,
                "longitude": None
            })

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

    print("Geolocation data saved successfully.")
else:
    print("Input file not found.")
