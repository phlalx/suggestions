import flask
import tree
import redis

query_tree = tree.build_tree('words.txt')

def counter():
    i = 0
    while True: 
        yield str(i)
        i += 1

def copy_tree_to_redis(tree):

    red = redis.Redis(host="localhost", db=0, socket_connect_timeout=2, socket_timeout=2)
    node_id_gen = counter()

    def fill_tree_redis(tree):

        node_id = next(node_id_gen)
        print(node_id, tree.suggestions.all(), tree.children)

        redis_value = {}
        redis_value['suggestions'] = " ".join(tree.suggestions.all())
        for letter, node in tree.children.items():
            redis_value[letter] = fill_tree_redis(node)

        red.hmset(node_id, redis_value)

        return node_id
        
    fill_tree_redis(tree)

app = flask.Flask(__name__, static_url_path='')

# copy_tree_to_redis(query_tree)

# res = red.hget(key, 'suggestions')

@app.route('/suggestions')
def suggestions():
    query = flask.request.args.get('query', default = '', type = str)
    red = redis.Redis(host="localhost", db=0, socket_connect_timeout=2, socket_timeout=2)
    tree = "0"
    res = ""

    for c in query:
        try:
            node = red.hget(tree, c)
        except Exception as e:
            print('redis exception', e)
            break

        if res is None:
            break
            
        tree = node
    
    if tree is not None:
        res = red.hget(tree, 'suggestions')

    return res

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
