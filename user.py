# Micro blogging - Bottle Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#

import sys
import textwrap
import logging.config
import sqlite3
import re


import bottle
from bottle import get, post, delete, error, abort, request, response, HTTPResponse
from bottle.ext import sqlite

#Set up app, plugins, and logging

app = bottle.default_app()
app.config.load_config('user.ini')

plugin = sqlite.Plugin(app.config['sqlite.dbfile'])
app.install(plugin)


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
@post('/user')
def createUser(db):
    creatingUser = request.json
    if not creatingUser:
        abort(400)
    posted_entry = creatingUser.keys()
    req_entry = {'username', 'password', 'email'}

    if not req_entry <= posted_entry:
        abort(400, f'Missing fields: {req_entry - posted_entry}')

    checkUsername = query(db, 'SELECT 1 FROM users WHERE username = ?', [creatingUser['username']])
    if len(checkUsername) == 1:
        abort(409, f'Username already exists')
    elif len(creatingUser['password']) < 8:
        abort(400, f'Password length is not 8 or greater')
    elif not re.search(r'\d', creatingUser['password']):
        abort(400, f'Password does not have at least a number in it')
    elif not re.match(r'\w*[A-Z]\w*', creatingUser['password']):
        abort(400, f'Password does not have at least an uppercase letter in it')
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", creatingUser['email']):
        abort(400, f'Invalid email')

    try:
        creatingUser['userID'] = execute(db, '''
        INSERT INTO user(username, password, email)
        VALUES(:username, :password, :email)
        ''', creatingUser)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))

    response.status = 201
    response.set_header('Location', f"/user{creatingUser['userID']}")

    return creatingUser

@get('/user/<username>/<password>')
def checkPassword(username, password, db):
    user = query(db, 'SELECT username, password FROM users WHERE (username = ? AND password = ?)', [username, password], one=True)
    if not user:
        abort(404)
    return {'status': 'true'}


@post('/user/follower/add')
def addFollower(db):
    addingFollower = request.json
    if not addingFollower:
        abort(400)

    posted_entry = addingFollower.keys()
    req_entry = {'username', 'follower'}

    if not req_entry <= posted_entry:
        abort(400, f'Missing fields: {req_entry - posted_entry}')

    try:
        userID = query(db, 'SELECT userID from users where username = ?', [addingFollower['username']], one=True)
        followerID = query(db, 'SELECT userID from users WHERE username = ?', [addingFollower['follower']], one=True)
        addingFollower['id'] = execute(db, f"INSERT INTO followers(userID, followerID) VALUES(\"{userID['userID']}\", \"{followerID['userID']}\")", addingFollower)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))

    response.status = 201
    response.set_header('Location', f"/user/follower/add{addingFollower['id']}")

    return addingFollower

@get('/user/<username>/follower/list')
def followingList(username, db):
    userID = query(db, 'SELECT userID from users WHERE username = ?', [username], one=True)
    if not userID:
        abort(404)

    followingUserDict = query(db, 'SELECT followerID from followers WHERE userID = ?', [userID['userID']])
    followingUserList = []

    for item in followingUserDict:
        followingUserList.append(item['followerID'])

    return {'followerList':followingUserList}



@delete("/user/follower/remove")
def removeFollower(db):
    removingFollower = request.json
    if not removingFollower:
        abort(400)

    posted_entry = removingFollower.keys()
    req_entry = {'username', 'follower'}

    if not req_entry <= posted_entry:
        abort(400, f'Missing fields: {req_entry - posted_entry}')

    try:
        userID = query(db, 'SELECT userID from users where username = ?', [removingFollower['username']], one=True)
        followerID = query(db, 'SELECT userID from users WHERE username = ?', [removingFollower['follower']], one=True)
        removingFollower['id'] = execute(db, f"DELETE FROM followers WHERE (userID = \"{userID['userID']}\" AND followerID = \"{followerID['userID']}\")", removingFollower)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))

    response.status = 201
    response.set_header('Location', f"/user/follower/remove{removingFollower['id']}")

    return removingFollower
