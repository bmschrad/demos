from helper import get_albums
from demo_data import users
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! I have been seen times.\n'

@app.route('/users')
def get_users():
    return json.dumps(users)

@app.route('/albums')
def get_all_albums():
    albums = get_albums()
    return json.dumps(albums)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
