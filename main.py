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

    courses = []
    ob1 = {}
    ob1["id"] = "001"
    ob1["name"] = "Advanced Topics of Software engineering"
    courses.append(ob1)

    ob2 = {}
    ob2["id"] = "002"
    ob2["name"] = "Artificial Intelligence"
    courses.append(ob2)

    ob3 = {}
    ob3["id"] = "003"
    ob3["name"] = "Machine Learning"
    courses.append(ob3)

    json_data = json.dumps(courses)

    return json_data


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
