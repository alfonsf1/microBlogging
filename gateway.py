#
# Simple API gateway in Python
#
# Inspired by <https://github.com/vishnuvardhan-kumar/loadbalancer.py>
#

from os import remove
import sys
import json
import http.client
import logging.config

import bottle
from bottle import route, request, response

import requests


# Allow JSON values to be loaded from app.config[key]
#
def json_config(key):
    value = app.config[key]
    return json.loads(value)


# Set up app and logging
#
app = bottle.default_app()
app.config.load_config('gateway.ini')

logging.config.fileConfig(app.config['logging.config'])

userPortList = json_config('users.userports')
# print("This is the user Port List: ", userPortList)
timelinePortList = json_config('timeline.timelineports')
# print("This is   global nthe timeline Port List: ", timelinePortList)




# If you want to see traffic being sent from and received by calls to
# the Requests library, add the following to etc/gateway.ini:
#
#   [logging]
#   requests = true
#
if json_config('logging.requests'):
    http.client.HTTPConnection.debuglevel = 1

    requests_log = logging.getLogger('requests.packages.urllib3')
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    logging.debug('Requests logging enabled')


# Return errors in JSON
#
# Adapted from <https://stackoverflow.com/a/39818780>
#
def json_error_handler(res):
    if res.content_type == 'application/json':
        return res.body
    res.content_type = 'application/json'
    if res.body == 'Unknown Error.':
        res.body = bottle.HTTP_CODES[res.status_code]
    return bottle.json_dumps({'error': res.body})


app.default_error_handler = json_error_handler


# Disable warnings produced by Bottle 0.12.19 when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    warnings.simplefilter('ignore', ResourceWarning)




n = -1
i = -1
def roundRobinCycle(list):
    global i
    global n
    if list == userPortList:
        n = n + 1
        return list[n % len(list)] 
    elif list == timelinePortList:
        i = i + 1
        return list[i % len(list)]




@route('<url:re:.*>', method='ANY')
def gateway(url):
    path = request.urlparts._replace(scheme='', netloc='').geturl()
    # print("This is the path: ", path)


    if "user" in path:
        nextPort = roundRobinCycle(userPortList)

    elif "timeline" in path:
        nextPort = roundRobinCycle(timelinePortList)
    print("Here is the next port: ", nextPort)

    upstream_servers = json_config('proxy.upstreams')
    upstream_server = upstream_servers[0]


    upstream_url = upstream_server + path
    logging.debug('Upstream URL: %s', upstream_url)

    headers = {}
    for name, value in request.headers.items():
        if name.casefold() == 'content-length' and not value:
            headers['Content-Length'] = '0'
        else:
            headers[name] = value

    try:
        upstream_response = requests.request(
            request.method,
            upstream_url,
            data=request.body,
            headers=headers,
            cookies=request.cookies,
            stream=True,
            
        )
        # print("Check here for upstream: ")
    except requests.exceptions.RequestException as e:
        logging.exception(e)
        response.status = 503

        if nextPort in userPortList:
            userPortList.remove(nextPort)

        elif nextPort in timelinePortList:
            timelinePortList.remove(nextPort)

        if not userPortList:
            response.status = 503
        elif not timelinePortList:
            response.status = 503
        return {
            'method': e.request.method,
            'url': e.request.url,
            'exception': type(e).__name__,
        }


    response.status = upstream_response.status_code
    for name, value in upstream_response.headers.items():
        if name.casefold() == 'transfer-encoding':
            continue
        response.set_header(name, value)
    return upstream_response.content
