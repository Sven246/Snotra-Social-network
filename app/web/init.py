from flask import Blueprint
from . import pages

def register_web_blueprints(app):
    web = Blueprint("web", __name__)

    pages.register(web)

    app.register_blueprint(web)
