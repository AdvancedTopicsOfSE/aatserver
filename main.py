from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

import json

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/courses')
def hello2():
    """Return a friendly HTTP greeting."""

    data = {}
    data['key'] = 'value'
    data['Hello'] = 'ciao'
    data['Hello2'] = 'ciao2'
    json_data = json.dumps(data)

    return json_data


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
