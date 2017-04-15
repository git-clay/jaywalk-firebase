"""File to seed firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
# import requests
from dotenv import load_dotenv, find_dotenv
from geopy.geocoders import Nominatim
from radius import get_radius
# from kineTable import build_categories_table, build_snap_table

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

firebase = pyrebase.initialize_app(config)
db = firebase.database()
# Get a reference to the auth service
# auth = firebase.auth()


"""Need to divide out table."""
"""Users, snaps, tags. Maybe more?"""


def snap_table(lines, context):
    """Loop through table from build_table."""
    new_list = context[0:lines]
    total_sent = 0
    snap_obj = {
        "snap_id": "",
        "title": "",
        "lat": "",
        "lng": "",
        "address": "",
        "radi": [],
        "location": [],
        "tag_ids": [],
        "description": "",
        "timestamp": "",
        "picture": "",
        "start_time": "",
        "end_time": "",
        "user_id": "",
        "business_hours": ""
    }
    geolocator = Nominatim()

    for line in new_list:
        """pushes to tag array"""
        for ids in line["category_details_id"]:
            snap_obj["tag_ids"].append(ids)

        """return address guess from geolocator"""
        lat = str(line['latitude'])
        lng = str(line['longitude'])
        location = geolocator.reverse(lat + "," + lng)

        """return 6 point radius from origin"""
        radius = get_radius(line["latitude"], line["longitude"])
        # print(line)
        """adding to object that is pushed to firebase"""
        snap_obj["snap_id"] = line["id"]
        snap_obj["title"] = line["title"]
        snap_obj["lat"] = lat
        snap_obj["lng"] = lng
        snap_obj["radi"] = radius
        snap_obj["address"] = line["address"]
        snap_obj["description"] = line["description"]
        snap_obj["timestamp"] = line["_created_ts"]
        snap_obj["picture"] = line["picture"]
        snap_obj["start_time"] = line["start_time"]
        snap_obj["end_time"] = line["end_time"]
        snap_obj["user_id"] = line["_author_id"]
        snap_obj["business_hours"] = line["openinghours"]
        snap_obj["location"] = location.address

        # pushes to firebase db
        db.child("snaps").child(line['id']).set(snap_obj)
        print (line['id'])
        total_sent = total_sent + 1
        print(str(total_sent) + " sent")

    return
