"""File to seed firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
import requests
# from flask import make_response
from dotenv import load_dotenv, find_dotenv
import firebase_admin
from firebase_admin import credentials

load_dotenv(find_dotenv())
apiKey = os.environ.get("apiKey")
authDomain = os.environ.get("authDomain")
databaseURL = os.environ.get("databaseURL")
storageBucket = os.environ.get("storageBucket")
project_id = os.environ.get("project_id")
token = os.environ.get("token")
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
auth = firebase.auth()


def templates_dir():
    """Might not need."""
    template_dir = "var/www/loader/loader/templates/"
    template_dir = "templates/"
    return template_dir


def build_url(command):
    """Create url to access kinetise."""
    host = "https://api-cms-fitrock.kinetise.com/"
    query = host + "api/kinetise/v2/projects/" + project_id + "/" + command + "access_token=" + token
    return query


def get_deal(deal_id):
    """Get deal."""
    query = build_url("tables/1/rows?id=" + deal_id + "&")
    res = requests.get(query)
# t_dir = templates_dir()
    o = res.json()
    row = o[0]
    try:
        category = row['category']['related_rows']
    except:
        category = 0

    context = {
        'title': 'WalkTo Deal',
        'description': row['description'],
        'openinghours': row['openinghours'],
        'picture': row['picture'],
        'address': row['address'],
        'latitude': row['latitude'],
        'longitude': row['longitude'],
        'venue_title': row['title'],
        'id': row['id'],
        'author_id': row['_author_id'],
        'category': category,
    }
    db.child("test").push(context)
    return context

print (get_deal('270'))
