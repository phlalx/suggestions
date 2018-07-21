import flask

app = flask.Flask(__name__, static_url_path='/static')

@app.route('/suggestions')
def suggestions():
    query = flask.request.args.get('query', default = "", type = str)
    return "query: " + "".join(reversed(query)) 

if __name__ == '__main__':
    app.run(debug=True)