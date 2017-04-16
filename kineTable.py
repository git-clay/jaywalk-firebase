"""Build api table to get info from kinetise."""
import os
import requests
from dotenv import load_dotenv, find_dotenv

from snapSeed import snap_table
from tagSeed import tag_table
from userSeed import user_table

# kinetise variables hidden in .env
load_dotenv(find_dotenv())
project_id = os.environ.get("project_id")
token = os.environ.get("token")


def build_url(command):
    """Create url to access kinetise."""
    host = "https://api-cms-fitrock.kinetise.com/"
    req_url = host + "api/kinetise/v2/projects/" + project_id + "/" + command + "access_token=" + token
    res = requests.get(req_url)
    res_obj = res.json()
    # print(res_obj)
    return res_obj


def build_categories_table():
    """Return category table from kinetise."""
    query = build_url("tables/5/rows/get-table?")

    category = query['results']   # category equals all snap objects
    lines = len(query['results'])  # lines equals number of objects in list

    tag_table(lines, category)
    return


def build_snap_table():
    """Return all snap objects in kinetise db."""
    query = build_url("tables/1/rows/get-table?")

    context = query['results']
    lines = len(query['results'])

    snap_table(lines, context)
    return


def build_user_table():
    """Return category table from kinetise."""
    query = build_url("users?")
    lines = len(query)
    user_table(lines, query)
    return


"""Uncomment 'build_categories_table' to seed tags object in db"""
# build_categories_table()

"""Uncomment 'build_snap_table' to seed snaps object in db"""
# build_snap_table()

"""Uncomment 'build_user_table' to seed users object in db"""
# build_user_table()
