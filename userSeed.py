"""File to seed firebase."""
# https://github.com/thisbejim/Pyrebase
import pyrebase
import os
from dotenv import load_dotenv, find_dotenv
# from kineTable import build_categories_table, build_user_table

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


def user_table(lines, context):
    """Loop through table from build_table."""
    new_list = context[0:lines]
    total_sent = 0
    user_obj = {
        "user_id": "",
        "business_type": "",
        "created": "",
        "devices": "",
        "first_name": "",
        "first_seen": "",
        "email": "",
        "email_subscription": "",
        "is_tracked": "",
        "last_name": "",
        "last_seen": "",
        "notifications": [],
        "picture": "",
        "role": "",
        "role_expiration": "",
        "social": [],
        "top_tags": [],
        "total_logins": [],
        "unsubscribe_token": [],
        "updated": ""
    }

    for line in new_list:
        """pushes to top_tag array"""
        # for ids in line["category_details_id"]:
        #     user_obj["tag_ids"].append(ids)

        """adding to object that is pushed to firebase"""
        user_obj["user_id"] = line["id"]
        user_obj["business_type"] = line["businesstype"]
        user_obj["created"] = line["created"]
        user_obj["devices"] = line["devices"]
        user_obj["first_name"] = line["first_name"]
        user_obj["first_seen"] = line["first_seen"]
        user_obj["email"] = line["email"]
        user_obj["email_subscription"] = line["email_subscription"]
        user_obj["is_tracked"] = line["istracked"]
        user_obj["last_name"] = line["last_name"]
        user_obj["last_seen"] = line["last_seen"]
        # user_obj["notifications"] = line["notifications"]
        user_obj["picture"] = line["picture"]
        user_obj["role"] = line["user_role"]
        # user_obj["role_expiration"] = line["role_expiration"]
        user_obj["social"] = line["social"]
        # user_obj["top_tags"] = line["top_tags"]
        user_obj["total_logins"] = line["total_logins"]
        user_obj["unsubscribe_token"] = line["unsubscribe_token"]
        user_obj["updated"] = line["_updated_ts"]

        # pushes to firebase db
        db.child("users").child(line['id']).set(user_obj)
        # print (line)
        total_sent = total_sent + 1
        # print(str(total_sent) + " sent")

    return
