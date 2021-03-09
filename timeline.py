# Micro blogging - Bottle Edition
#
# Adapted from "Creating Web APIs with Python and Flask"
# <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>.
#

import sys
import textwrap
import logging.config
import sqlite3


import bottle
from bottle import get, post, error, abort, request, response, HTTPResponse
from bottle.ext import sqlite

#Set up app, plugins, and logging

app = bottle.default_app()
app.config.load_config('timeline.ini')

plugin2 = sqlite.Plugin(app.config['sqlite.dbfile2'])
app.install(plugin2)

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
#user, posts, timeline
######################Routes#####################

#http GET localhost:5100/timeline/Alfonso
@get('/timeline/<username>')
def getUserTimeline(username, db):
    userPost = query(db, 'SELECT author, text, postID, timestamp FROM posts WHERE author = ? ORDER BY postID desc LIMIT 25', [username])
    if not userPost:
        abort(404)
    print(userPost)
    # userTimeline = userPost.reverse()
    return {'user_timeline': userPost}
    


#http GET localhost:5100/timeline/public
@get('/timeline/public')
def getPublicTimeline(db):
    public_timeline = query(db, 'SELECT author, text, postID, timestamp from posts ORDER BY postID desc LIMIT 25')

    return {'public_timeline': public_timeline}


#http GET localhost:5100/timeline/home/Alfonso
@get('/timeline/home/<username>')
def getHomeTimeline(username, db):
    userDB = sqlite3.connect('user.db')
    homeTimeLine = {'home_timeline': []}
    try:
        userID = query(userDB, 'SELECT userID FROM users WHERE username = ?', [username], one = True)
        followingID = query(userDB, 'SELECT followerID from followers WHERE userID = ?', [userID['userID']])
        for id in followingID: 
            post = query(db, 'SELECT postID, author, text, timestamp FROM posts WHERE userID = ? ORDER BY postID desc LIMIT 25', [id['followerID']])
            for post in post:
                homeTimeLine['home_timeline'].append(post)
                if len(homeTimeLine['home_timeline']) == 25:
                    break
    except sqlite3.IntegrityError as e:
        abort(409, str(e))
    sorted_timeline = sorted(homeTimeLine['home_timeline'], key=lambda d: (d['postID'], d['timestamp']), reverse= True)
    homeTimeLine['home_timeline'] = sorted_timeline
    return homeTimeLine

#http POST localhost:5100/timeline/post author="Alfonso" postText="Hello!, My name is Alfonso!"
@post('/timeline/create')
def postTweet(db):
    userDB = sqlite3.connect('user.db')
    createTweet = request.json
    if not createTweet:
        abort(400)

    posted_entry=createTweet.keys()
    req_entry={'author', 'postText'}

    if not req_entry <= posted_entry:
        abort(400, f'Missing fields: {req_entry - posted_entry}')
    
    try:
         userID = query(userDB, 'SELECT userID from users WHERE username = ?', [createTweet['author']], one=True)
         createTweet['postID'] = execute(db, f'''INSERT INTO posts(author, text, userID) 
         VALUES(\"{createTweet['author']}\", \"{createTweet['text']}\", \"{userID['userID']}\")''', createTweet)
    except sqlite3.IntegrityError as e:
        abort(409, str(e))
    response.status = 201
    response.set_header('Location', f"/timeline/create{createTweet['postID']}")

    return createTweet
