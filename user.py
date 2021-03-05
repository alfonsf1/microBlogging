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
app.config.load_config('user.ini')

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
# http post localhost:5000/createUser username='Sergio' password='xyz789' email='Sergio@gmail.com'
@post('/createUser')
def createUser(db):
    #Registers a new user account. Returns true if username i
    creatingUser = request.json
    if not creatingUser:
        abort(400)

    posted_entry = creatingUser.keys()
    req_entry = {'username', 'password', 'email'}

    if not req_entry <= posted_entry:
        abort(400, f'Missing fields: {req_entry - posted_entry}')

    try:
        creatingUser['userID'] = execute(db, '''
        INSERT INTO user(username, password, email)
        VALUES(:username, :password, :email)
        ''', creatingUser)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))

    response.status = 201
    response.set_header('Location', f"/createUser{creatingUser['userID']}")

    return creatingUser
 
# http localhost:5000/checkPassword/Alfonso/abc123
@get('/checkPassword/<username>/<password>')
def checkPassword(username, password, db):
    user = query(db, 'SELECT username, password FROM user WHERE (username = ? AND password = ?)', [username, password], one=True)
    if not user:
        abort(404)
    #Returns true if the password parameter matches the password stored for the username.
    return {'status': 'true'}

@post('/addFollower')
def addFollower(db):
    addingFollower = request.json
    if not addingFollower:
        abort(400)

    posted_entry = addingFollower.keys()
    req_entry = {'username', 'follower'}

    #reqEntryList = list(req_entry)
    



  

    if not req_entry <= posted_entry:
        abort(400, f'Missing fields: {req_entry - posted_entry}')

    try:
        userID = query(db, 'SELECT userID from user where username = ?', [addingFollower['username']], one=True)
        followerID = query(db, 'SELECT userID from user WHERE username = ?', [addingFollower['follower']], one=True)
        print(userID)
        print(followerID)
        addingFollower['id'] = execute(db, f"INSERT INTO followers(userID, followingID) VALUES(\"{userID['userID']}\", \"{followerID['userID']}\")", addingFollower)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))

    response.status = 201
    response.set_header('Location', f"/createUser{addingFollower['id']}")

    return addingFollower
    #Start following a new user.
    #pass


@app.route("/removeFollower", methods=['PUT'])
def removeFollower(username, usernameToRemove):
    #Stop following a user.
    pass










@get('/seeAllData')
def seeAllData(db):
    #see all data
    all_user = query(db, 'SELECT * FROM user;')
    all_followers = query(db, 'SELECT * FROM followers;')
    all_post = query(db, 'SELECT * FROM post;')
    
    return {'user': all_user, 'followers': all_followers, 'post': all_post}