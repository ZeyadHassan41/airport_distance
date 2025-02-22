from math import radians, sin, cos, sqrt, atan2
from .models import Airport

def calculate_distance(iata1, iata2):
    try:
        airport1 = Airport.objects.get(iata_code=iata1.upper())
        airport2 = Airport.objects.get(iata_code=iata2.upper())
    except Airport.DoesNotExist:
        return None #Handle missing airport
    
    lat1, lon1 = radians(airport1.latitude), radians(airport1.longitude)
    lat2, lon2 = radians(airport2.latitude), radians(airport2.longitude)

    dlon = lon2- lon1
    dlat = lat2- lat1
    haversine_value = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    central_angle = 2 * atan2(sqrt(haversine_value), sqrt(1 - haversine_value))

    radius = 6371  # Earth's radius in km
    distance = radius * central_angle  # Corrected calculation

    return distance
# Renamed a → haversine_value (to indicate it's the result of the Haversine formula calculation).
# Renamed c → central_angle (since it represents the central angle in radians).
# Renamed R → RADIUS_EARTH_KM for better clarity.
# Renamed dlat and dlon → delta_lat and delta_lon (to explicitly mean "difference in latitude/longitude").