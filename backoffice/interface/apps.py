from flask import Flask
from backoffice.interface.login import create_login


def create_app():
    app = Flask(__name__)

    login_apis = create_login(app=app)

    app.register_blueprint(login_apis, url_prefix='/api/v1')
    return app