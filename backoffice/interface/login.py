from backoffice.service import user_load

import os
from flask_login import LoginManager, logout_user, login_required, current_user, login_user
from flask import Blueprint, request, jsonify




def create_login(app):
    app.config['TESTING'] = True
    login_bf = Blueprint('login_api', __name__)
    app.secret_key = os.urandom(24)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user):
        print(user)
        login_user(user, remember=True)
        return user

    @login_bf.route('/login', methods=['GET'])
    def login():
        user = dict()
        user['id'] = request.args.get('user_id', '')
        user['password'] = request.args.get('user_password', '')
        result = user_load(login=user)
        load_user(user=result)
        return jsonify({"ok": True})

    @login_bf.route('/logout', methods=['GET'])
    @login_required
    def logout():
        logout_user()
        return jsonify({"answer": True})

    @login_bf.route('/logincheck', methods=['GET'])
    @login_required
    def logincheck():
        user = current_user
        json_res = {'ok': True, 'msg': 'auth_func(%s),user_id=%s'
                                       % (request.json, user.user_id)}
        return jsonify(json_res)

    return login_bf