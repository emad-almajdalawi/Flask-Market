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


main = blueprints.Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    return "<p>home page</p>"
