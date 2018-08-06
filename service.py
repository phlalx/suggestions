import flask
import redis
import mapreduce

app = flask.Flask(__name__, static_url_path='')

from flask import g

def get_db():
    if 'db' not in g:
        g.db = redis.Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
    return g.db

@app.route('/filldb')
def fill_db():
    try:
        mapreduce.fill_redis()
    except Exception as e:
        return str(e)
    return "Done"
    
@app.route('/suggestions')
def suggestions():
    query = flask.request.args.get('query', default = '', type = str)
    red = get_db()
    res = red.get(query)
    if res is None:
        return ""
    else:
        return res

@app.route('/getkey')
def getkey():
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
