from flask_login import LoginManager, logout_user
from flask import Blueprint, request

login_manager = LoginManager()


def create_login(app):
    login_bf = Blueprint('login_api', __name__)
    login_manager.init_app(app)

    @login_bf.route('/login')
    @login_manager.user_loader
    def load_user():
        user_id = request.args.get('user_id')
        return user_id

    @login_bf.route('/logout')
    def logout():
        logout_user()

    return login_bf