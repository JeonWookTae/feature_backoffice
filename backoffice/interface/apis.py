from flask import Blueprint


def create_app(app):
    bf = Blueprint('backoffice', __name__)
    return bf