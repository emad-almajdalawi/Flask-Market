# this file could be renamed to be (__init__.py) to make the project a package
# then create run.py file to run the app and put in it (app.run(debug=True))
# also template files could be moved inside each blueprint folder (auth and main)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


template_dir = os.path.join(os.path.dirname(__name__), "templates")
app = Flask(__name__, template_folder=template_dir)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

# with app.app_context():
#     db.create_all()

from auth.views import sign
from main.views import main

app.register_blueprint(sign)
app.register_blueprint(main)


app.secret_key = "super secret key"
