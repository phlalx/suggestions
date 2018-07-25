import flask
import redis

app = flask.Flask(__name__, static_url_path='')

@app.route('/getkey')
def getkey():
    # TODO set up connection somewhere else
    key = flask.request.args.get('key', default = '', type = str)
    res = None
    try:
        red = redis.Redis(host="localhost", db=0, socket_connect_timeout=2, socket_timeout=2)
        res = red.get(key)
    except Exception as e:
        print("cant't access redis", e)
        pass
    if res is None:
        res = "unkown"
    return res

@app.route('/setkeyvalue')
def setkeyvalue():
    key = flask.request.args.get('key', default = '', type = str)
    value = flask.request.args.get('value', default = '', type = str)
    # TODO set up connection somewhere else
    try:
        red = redis.Redis(host="localhost", db=0, socket_connect_timeout=2, socket_timeout=2)
        red.set(key, value)
    except Exception as e:
        print("cant't access redis", e)
        pass

    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # default port = 5000
