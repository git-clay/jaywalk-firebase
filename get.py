"""File to get info from firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
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

firebase = pyrebase.initialize_app(config)
db = firebase.database()
# Get a reference to the auth service
# auth = firebase.auth()
