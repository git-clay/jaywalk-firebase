"""File to get info from firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
from dotenv import load_dotenv, find_dotenv

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
tags = db.child('tags')


"""Query examples to get info."""
# all_objects = tags.get()  # gets all objects
all_objects_by_key = tags.child('Bakery').get()

print(all_objects_by_key.val())
