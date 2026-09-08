from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="fiap_python_foundations")
address = input("Enter an address: ")
location = geolocator.geocode(address)

if location is not None:
    print("Address....: ", location.address)
    print("Latitude...: ", location.latitude)
    print("Longitude..: ", location.longitude)
else:
    print("Location not found.")
