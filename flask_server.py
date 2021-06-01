import os

from flask import Flask, jsonify, make_response, send_from_directory, request, abort

import utils

app = Flask(__name__)

users = [
    {
        "test1": {
            "password": "3d309097bbbe6478f483bc80943a1141b2a6eb22c1767bdeb7e33e405bb7c744eb4b221176a3b72a9786b53e4c9cb69dcef32f5ab46f0a71e1a80612f004d9478231dfcf1a33ef44b8e86259cc4b610a2b636e9ac48bb9a0a7dfb80d9f276b68",
            "registration_date": "127.0.0.1"
        }
    }
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users', methods=['GET'])
def get_users():
    with open("../9-Task/users.json", "r") as f:
        return f.read(), 200


@app.route('/users', methods=['POST'])
def add_user():
    if not request.json or not 'login' in request.json:
        abort(400)
    utils.add_user(request.json['login'], request.json['password'])
    return utils.get_user_by_login(request.json['login']), 201


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
