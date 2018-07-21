import flask
import tree

query_tree = tree.build_tree('words.txt')

app = flask.Flask(__name__, static_url_path='/static')

@app.route('/suggestions')
def suggestions():
    query = flask.request.args.get('query', default = "", type = str)
    if query_tree.startsWith(query):
        res = "{} is in my dictionary".format(query)
    else:
        res = "{} is not in my dictionary".format(query)
    return res

if __name__ == '__main__':
    app.run(debug=True)