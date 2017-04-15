"""File to get info from firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
# from haversine import haversine
import math
# from flask import make_response
from dotenv import load_dotenv, find_dotenv

# import firebase_admin
# from firebase_admin import credentials

# firebase variables hidden in .env
load_dotenv(find_dotenv())
apiKey = os.environ.get("apiKey")
authDomain = os.environ.get("authDomain")
databaseURL = os.environ.get("databaseURL")
storageBucket = os.environ.get("storageBucket")


# config for pyrebase/firebase keys
config = {
    "apiKey": apiKey,
    "authDomain": authDomain,
    "databaseURL": databaseURL,
    "storageBucket": storageBucket,
    "serviceAccount": "./serviceAccount.json"
}

# distance calc variables
radius = 500.0  # 0.5km or 2.2 mile total diameter
centerLat = 30.0
centerLng = -100.0
numPoints = 6


firebase = pyrebase.initialize_app(config)
db = firebase.database()
tags = db.child('tags')

# 1˚ lat= ~69miles (range 68.7 @ equator ->69.4 @ poles)
# 1˚ lng= 69.17miles @ equator-> 53miles@40˚lat -> 0 at poles

# haversine gets distance between two points
# lyon = (45.7597, 4.8422)
# paris = (48.8567, 2.3508)
# print(haversine(lyon, paris, miles=True))

circlePoints = []
for k in range(numPoints):
    """Return 6 points at 1 km distance from origin."""
    angle = math.pi * 2 * k / numPoints
    dx = radius * math.cos(angle)
    dy = radius * math.sin(angle)
    point = {}
    point['lat'] = centerLat + (180 / math.pi) * (dy / 6378137)
    point['lng'] = centerLng + (180 / math.pi) * (dx / 6378137) / math.cos(centerLat * math.pi / 180)
    circlePoints.append(point)

# print (circlePoints)

"""Query examples to get info."""
# all_objects = tags.get()  # gets all objects
all_objects_by_key = tags.child('Bakery').get()

print(all_objects_by_key.val())
