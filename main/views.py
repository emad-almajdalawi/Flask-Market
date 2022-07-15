from flask import (
    blueprints,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)
from flask import abort, flash


main = blueprints.Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    return render_template("main/home.html", title="Home")


@main.route("/about", methods=["GET"])
def about():
    return render_template("main/about.html", title="About")


@main.route("/market", methods=["GET"])
def market():
    return render_template("main/market.html", title="Market")
