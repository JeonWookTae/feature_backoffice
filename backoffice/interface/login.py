from backoffice.service import user_load, user_id_load, user_login_valid_check

import os
from flask_login import LoginManager, logout_user, login_required, current_user, login_user
from flask import Blueprint, request, jsonify


def create_login(app):
    login_bf = Blueprint('login_api', __name__)
    app.secret_key = os.urandom(24)
    login_manager = LoginManager()
    login_manager.init_app(app)

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
        print(json_result)
        return jsonify(json_result)

    @login_bf.route('/logout', methods=['GET'])
    @login_required
    def logout():
        logout_user()
        return jsonify({"ok": True, 'msg': 'success'})

    @login_bf.route('/logincheck', methods=['GET'])
    @login_required
    def authou():
        user = current_user
        json_res = {'ok': True, 'msg': 'success'}
        return jsonify(json_res)

    return login_bf
