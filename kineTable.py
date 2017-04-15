"""Build api table to get info from kinetise."""
import os
import requests
from dotenv import load_dotenv, find_dotenv

from snapSeed import snap_table
from tagSeed import tag_table

# kinetise variables hidden in .env
load_dotenv(find_dotenv())
project_id = os.environ.get("project_id")
token = os.environ.get("token")


def build_url(command):
    """Create url to access kinetise."""
    host = "https://api-cms-fitrock.kinetise.com/"
    query = host + "api/kinetise/v2/projects/" + project_id + "/" + command + "access_token=" + token
    return query


def build_snap_table():
    """Return all snap objects in kinetise db."""
    query = build_url("tables/1/rows/get-table?")
    res = requests.get(query)
    o = res.json()
    # context equals all snap objects
    context = o['results']
    # lines equals number of objects in list
    lines = len(o['results'])

    snap_table(lines, context)
    return


def build_categories_table():
    """Return category table from kinetise."""
    query = build_url("tables/5/rows/get-table?")
    res = requests.get(query)
    o = res.json()
    category = o['results']

    lines = len(o['results'])
    tag_table(lines, category)
    return

"""Uncomment 'build_categories_table' to seed tags object in db"""
# build_categories_table()

"""Uncomment 'build_snap_table' to seed snaps object in db"""
build_snap_table()

"""Uncomment 'build_user_table' to seed users object in db"""
# build_user_table()
