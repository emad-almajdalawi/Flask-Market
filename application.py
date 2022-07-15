from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    template_dir = os.path.join(os.path.dirname(__name__), "templates")
    app = Flask("Flask-Market", template_folder=template_dir)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from auth.views import sign
    from main.views import main

    app.register_blueprint(sign)
    app.register_blueprint(main)

    return app
