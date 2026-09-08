from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="fiap_python_foundations")
latitude = input("Enter the latitude: ")
longitude = input("Enter the longitude: ")
coordinates = latitude + ", " + longitude
location = geolocator.reverse(coordinates)

if location is not None:
    print("Address: ", location.address)
else:
    print("Location not found.")
