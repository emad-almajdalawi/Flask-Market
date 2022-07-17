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


@sign.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():  # if form is submitted (POST)
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if not username or not email or not password:
            flash("Please fill all fields")
            return redirect(url_for("sign.signup"))
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("sign.signin"))  # redirect to signin page

    if form.errors != {}:
        for error in form.errors:
            flash(form.errors[error][0], category="danger")
    return render_template("auth/signup.html", title="Sign Up", form=form)  # GET


@sign.route("/signin", methods=["GET", "POST"])
def signin():
    form = LoginForm()

    if form.validate_on_submit():  # if form is submitted (POST)
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if not user:
            flash("User not found")
            return redirect(url_for("sign.signin"))
        if user.password != password:
            flash("Wrong password")
            return redirect(url_for("sign.signin"))
        session["user_id"] = user.id
        return redirect(url_for("main.home"))  # redirect to home page

    if form.errors != {}:
        for error in form.errors:
            flash(form.errors[error][0], category="danger")

    return render_template("auth/signin.html", title="Sign In", form=form)  # GET


@sign.route("/signout")
def signout():
    return redirect(url_for("sign.signin"))
