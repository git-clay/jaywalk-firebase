"""Return radius from lat/lng or havesine to get distance point a->b."""
# from haversine import haversine
import math

# distance calc variables
radius = 500.0  # 0.5km or 2.2 mile total diameter

numPoints = 6
circlePoints = []


def get_radius(lat, lng):
    """Return 6 points at 1 km distance from origin."""
    center_lat = lat
    center_lng = lng
    for k in range(numPoints):
        angle = math.pi * 2 * k / numPoints
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        point = {}
        point['lat'] = center_lat + (180 / math.pi) * (dy / 6378137)
        point['lng'] = center_lng + (180 / math.pi) * (dx / 6378137) / math.cos(center_lat * math.pi / 180)
        circlePoints.append(point)

    # print (circlePoints)
    return circlePoints

# 1˚ lat= ~69miles (range 68.7 @ equator ->69.4 @ poles)
# 1˚ lng= 69.17miles @ equator-> 53miles@40˚lat -> 0 at poles

# haversine gets distance between two points
# lyon = (45.7597, 4.8422)
# paris = (48.8567, 2.3508)
# print(haversine(lyon, paris, miles=True))
