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
from auth.forms import SignupForm, LoginForm


sign = blueprints.Blueprint("sign", __name__)


@sign.route("/signup", methods=["GET"])
def signup():
    form = SignupForm()
    return render_template("auth/signup.html", title="Sign Up", form=form)


@sign.route("/signup", methods=["POST"])
def signup_post():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    if not name or not email or not password:
        flash("Please fill all fields")
        return redirect(url_for("sign.signup_post"))

    new_user = User(username, email, password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("sign.signin"))

    # form = SignupForm(request.form)
    # if not form.validate():
    #     flash("Please fill all fields")
    #     return redirect(url_for("sign.signup_post"))


@sign.route("/signin", methods=["GET"])
def signin():
    form = LoginForm()
    return render_template("auth/signin.html", title="Sign In", form=form)


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
