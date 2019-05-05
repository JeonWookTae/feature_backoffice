from backoffice.service import user_id_load, user_login_valid_check, unauthorized_return

import os
from flask_login import LoginManager, logout_user, login_required, current_user, login_user
from flask_cache import Cache
from flask import Blueprint, request, jsonify


def create_secret_key():
    return os.urandom(24)


def create_login(app):
    login_bf = Blueprint('login_api', __name__)
    app.secret_key = b'#t\xd5\x90\x97\xfd~A\x94bc(p\x89\x10\xd3\xd6\xc1\xa0\xb4\xa8\n,\xb8'
    login_manager = LoginManager()
    login_manager.unauthorized_handler(unauthorized_return)
    login_manager.init_app(app)
    # cache = Cache(app, config={'CACHE_TYPE': 'simple'})

    @login_manager.user_loader
    def load_user(user_id):
        user = user_id_load(login=user_id)
        return user

    @login_bf.route('/login', methods=['GET'])
    def login():
        login_rq = dict()
        login_rq['id'] = request.args.get('user_id', '')
        login_rq['password'] = request.args.get('user_password', '')
        json_result = user_login_valid_check(login_rq.get('id'), login_rq.get('password'))
        return jsonify(json_result)

    @login_bf.route('/signup', methods=['POST'])
    def signup():
        pass

    @login_bf.route('secession', methods=['DELETE'])
    def secession():
        pass

    @login_bf.route('/logout', methods=['GET'])
    @login_required
    def logout():
        logout_user()
        return jsonify({"ok": 200, 'msg': 'success'})

    @login_required
    @login_bf.route('/authenticate', methods=['GET'])
    def authenticate():
        json_res = {'ok': 200, 'msg': 'authenticate success'}
        return jsonify(json_res)

    return login_bf
