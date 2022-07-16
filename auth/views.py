from hashlib import new
from unicodedata import name
from flask import (
    blueprints,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
from auth.models import User
from application import db


sign = blueprints.Blueprint("sign", __name__)


@sign.route("/signup", methods=["GET"])
def signup():
    return render_template("auth/signup.html", title="Sign Up")


@sign.route("/signup", methods=["POST"])
def signup_post():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    if not name or not email or not password:
        flash("Please fill all fields")
        return redirect(url_for("sign.signup_post"))

    new_user = User(name, email, password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("sign.signin"))


@sign.route("/signin", methods=["GET"])
def signin():
    return render_template("auth/signin.html", title="Sign In")


@sign.route("/signin", methods=["POST"])
def signin_post():
    name = request.POST.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password or not name:
        flash("Please fill all fields")
        return redirect(url_for("sign.signin_post"))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash("User not found")
        return redirect(url_for("sign.signin_post"))

    if user.password != password:
        flash("Wrong password")
        return redirect(url_for("sign.signin_post"))

    session["user_id"] = user.id
    return redirect(url_for("main.home"))


@sign.route("/signout", methods=["POST"])
def signout():
    return redirect(url_for("sign.signin"))
