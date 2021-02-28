# Micro blogging - Bottle Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#

import sys
import textwrap
import logging.config
import sqlite3
import pandas as pd


import bottle
from bottle import get, post, error, abort, request, response, HTTPResponse
from bottle.ext import sqlite

#Set up app, plugins, and logging

app = bottle.default_app()
app.config.load_config('api.ini')

plugin = sqlite.Plugin(app.config['sqlite.dbfile'])
app.install(plugin)

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect('schema.db')
#         print("Database connected")
#     return db


#logging.config.fileConfig(app.config['logging.config'])


# Return errors in JSON
#
# Adapted from # <https://stackoverflow.com/a/39818780>
#
def json_error_handler(res):
    if res.content_type == 'application/json':
        return res.body
    res.content_type = 'application/json'
    if res.body == 'Unknown Error.':
        res.body = bottle.HTTP_CODES[res.status_code]
    return bottle.json_dumps({'error': res.body})


app.default_error_handler = json_error_handler

# Disable warnings produced by Bottle 0.12.19.
#
#  1. Deprecation warnings for bottle_sqlite
#  2. Resource warnings when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    for warning in [DeprecationWarning, ResourceWarning]:
        warnings.simplefilter('ignore', warning)


# Simplify DB access
#
# Adapted from
# <https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/#easy-querying>
#
def query(db, sql, args=(), one=False):
    cur = db.execute(sql, args)
    rv = [dict((cur.description[idx][0], value)
          for idx, value in enumerate(row))
          for row in cur.fetchall()]
    cur.close()

    return (rv[0] if rv else None) if one else rv


def execute(db, sql, args=()):
    cur = db.execute(sql, args)
    id = cur.lastrowid
    cur.close()

    return id

#Routes

#USER SERVICE
@get('/createUser')
def createUser(db):
    #Registers a new user account. Returns true if username i
    all_books = query(db, 'SELECT * FROM user;')
    
    return {'user': all_books}

    
 

@app.route("/checkPassword", methods=['GET'])
def checkPassword(username, password):
    #Returns true if the password parameter matches the password stored for the username.
    pass

@app.route("/addFollower", methods=['PUT'])
def addFollower(username, usernameToFollow):
    #Start following a new user.
    pass


@app.route("/removeFollower", methods=['PUT'])
def removeFollower(username, usernameToRemove):
    #Stop following a user.
    pass


def getUserTimeline(username):
    #first check if user is in db
    #if not, return error
    #else find the post with the most recent date
    pass
def getPublicTimelinme():
    #first, check if user is in db
    #if not, return error
    #else return all the post from that user
    pass
def getHomeTimeline(username):
    #first, checkf if user is in db
    #if not, return error
    #else return recent posts from all the users that this user is following
    pass
def postTweet(username, text):
    #first check if the ussername exist
    #if not, error
    #else, post the new tweet
    pass