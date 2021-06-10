from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from environs import Env
from app import views


# ----------------------------------------------
env = Env()
env.read_env()

db = SQLAlchemy()
# ----------------------------------------------


def create_app() -> Flask:

    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    views.init_app(app)

    with app.app_context():
        db.create_all()

    return app


# ----------------------------------------------
