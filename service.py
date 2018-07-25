import flask
import redis

app = flask.Flask(__name__, static_url_path='')

from flask import g

def get_db():
    if 'db' not in g:
        g.db = redis.Redis(host="localhost", db=0, socket_connect_timeout=2, socket_timeout=2)
    return g.db

@app.route('/getkey')
def getkey():
    # TODO set up connection somewhere else
    key = flask.request.args.get('key', default = '', type = str)
    red = get_db()
    res = red.get(key)
    if res is None:
        res = 'unknown'
    return res

@app.route('/setkeyvalue')
def setkeyvalue():
    key = flask.request.args.get('key', default = '', type = str)
    value = flask.request.args.get('value', default = '', type = str)
    red = get_db()
    red.set(key, value)
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # default port = 5000
