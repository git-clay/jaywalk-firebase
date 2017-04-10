"""File to seed firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
import requests
# from flask import make_response
from dotenv import load_dotenv, find_dotenv
from geopy.geocoders import Nominatim

# import firebase_admin
# from firebase_admin import credentials

# firebase variables hidden in .env
load_dotenv(find_dotenv())
apiKey = os.environ.get("apiKey")
authDomain = os.environ.get("authDomain")
databaseURL = os.environ.get("databaseURL")
storageBucket = os.environ.get("storageBucket")
# kinetise variables hidden in .env
project_id = os.environ.get("project_id")
token = os.environ.get("token")

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


def build_url(command):
    """Create url to access kinetise."""
    host = "https://api-cms-fitrock.kinetise.com/"
    query = host + "api/kinetise/v2/projects/" + project_id + "/" + command + "access_token=" + token
    return query


def build_table():
    """Return all snap objects in kinetise db."""
    query = build_url("tables/1/rows/get-table?")
    res = requests.get(query)
    o = res.json()
    # context equals all snap objects
    context = o['results']
    # lines equalts number of objects in list
    lines = len(o['results'])
    manage_deals(lines, context)
    return context


def manage_deals(lines, context):
    """Loop through table from build_table."""
    new_list = context[0:lines]
    total_sent = 0

    geolocator = Nominatim()

    for lines in new_list:
        if lines['_author_email'] is None:
            email = ""
        else:
            email = lines["_author_email"]
        if lines['_author_first_name'] is None:
            first_name = ""
        else:
            first_name = lines['_author_first_name']

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
        # location.raw is an object that returns address estimation
        # fix_address(location, lines['id'],lat,lon,title)
        
        # pushes to firebase db
        db.child("test2").push(lines)
        print (lines)
        try:
            location.address
        except NoneType:
            loc = "Unknown address"
        else:
            loc = location.address

        total_sent = total_sent + 1

    return str(total_sent) + " sent"
build_table()
# need to create loop to get each snap from kinetise
