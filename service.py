import flask
import tree

query_tree = tree.build_tree('words.txt')

app = flask.Flask(__name__, static_url_path='')

@app.route('/suggestions')
def suggestions():
    query = flask.request.args.get('query', default = "", type = str)
    node = query_tree.startsWith(query)
    if node is not None:
        res = " ".join( node.suggestions.all() )
    else:
        res = ""
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # default port = 5000
