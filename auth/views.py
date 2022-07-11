from flask import (
    blueprints,
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
)
from flask import abort, flash


sign = blueprints.Blueprint("sign", __name__)


@sign.route("/signup", methods=["GET", "POST"])
def signup():
    return "<p>Signup page</p>"


@sign.route("/signin", methods=["GET", "POST"])
def signin():
    return "<p>Signin page</p>"


@sign.route("/signout", methods=["GET", "POST"])
def signout():
    return "<p>Signout page</p>"
