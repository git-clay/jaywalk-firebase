"""File to seed firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
# import requests
from dotenv import load_dotenv, find_dotenv
from geopy.geocoders import Nominatim

# from kineTable import build_categories_table, build_snap_table

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

firebase = pyrebase.initialize_app(config)
db = firebase.database()
# Get a reference to the auth service
# auth = firebase.auth()


"""Need to divide out table."""
"""Users, snaps, tags. Maybe more?"""


def snap_table(lines, context):
    """Loop through table from build_table."""
    new_list = context[0:1]
    total_sent = 0
    snap_obj = {
        "snap_id": "",
        "title": "",
        "lat": "",
        "lng": "",
        "address": "",
        "radi": "",
        "tags": "",
        "description": "",
        "timestamp": "",
        "address": "",
        "pic": "",
        "start_time": "",
        "end_time": "",
        "user_id": "",
        "business_name": ""
    }
    geolocator = Nominatim()

    for lines in new_list:

        # snap_obj['tag_id'] = lines['id']
        # snap_obj['name'] = lines['name']
        # snap_obj['total_used'] = ''
        # snap_obj['locations_used'] = []
        # snap_obj['days_ranked'] = []
        # snap_obj['times_ranked'] = []
        # snap_obj['pin'] = lines['pin']
        # snap_obj['free_pin'] = lines['free_pin']
        if lines['_author_id'] is None:
            first_name = ""
        else:
            userId = lines['_author_id']

        cat = lines['category_details_name']

        picture = lines['picture']
        id = lines['id']

        if lines['description'] is None:
            descr = "Spotted in the wild"
        else:
            descr = lines['description']

        try:
            lines['title']
        except NoneType:
            title = "None"
        else:
            title = lines['title']

        lat = str(lines['latitude'])
        lon = str(lines['longitude'])
        location = geolocator.reverse(lat + "," + lon)

        # pushes to firebase db
        # db.child("testsnaps").child(lines['id']).set(lines)
        print (lines)
        try:
            location.address
        except NoneType:
            loc = "Unknown address"
        else:
            loc = location.address

        total_sent = total_sent + 1

    return str(total_sent) + " sent"
