"""Seed user object in firebase."""
import pyrebase
import os
from dotenv import load_dotenv, find_dotenv


"""firebase variables hidden in .env"""
load_dotenv(find_dotenv())
apiKey = os.environ.get("apiKey")
authDomain = os.environ.get("authDomain")
databaseURL = os.environ.get("databaseURL")
storageBucket = os.environ.get("storageBucket")

"""config for pyrebase/firebase keys"""
config = {
    "apiKey": apiKey,
    "authDomain": authDomain,
    "databaseURL": databaseURL,
    "storageBucket": storageBucket,
    "serviceAccount": "./serviceAccount.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def user_table(lines, context):
    """Loop through table from build_table."""
    new_list = context[0:lines]
    total_sent = 0

    tag_obj = {
        "tag_id": '',
        "name": '',
        "total_used": '',
        "locations_used": [],
        "days_ranked": [],
        "times_ranked": [],
        "pin": '',
        "free_pin": ''
    }

    for lines in new_list:
        tag_obj['tag_id'] = lines['id']
        tag_obj['name'] = lines['name']
        tag_obj['total_used'] = ''
        tag_obj['locations_used'] = []
        tag_obj['days_ranked'] = []
        tag_obj['times_ranked'] = []
        tag_obj['pin'] = lines['pin']
        tag_obj['free_pin'] = lines['free_pin']

        print(tag_obj)
        db.child('tags').child(tag_obj['name']).set(tag_obj)
        total_sent = total_sent + 1

    return str(total_sent) + " sent"
