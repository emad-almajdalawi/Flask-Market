from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask("Flask-Market")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)

    from auth.views import sign
    from main.views import main

    app.register_blueprint(sign)
    app.register_blueprint(main)

    return app
