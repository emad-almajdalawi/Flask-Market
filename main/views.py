from flask import (
    blueprints,
    render_template,
    request,
    redirect,
    url_for,
)
from flask import abort, flash
from main.models import Product
from application import db


main = blueprints.Blueprint("main", __name__)

global products
products = Product.query.all()


@main.route("/", methods=["GET"])
def home():
    return render_template("main/home.html", title="Home")


@main.route("/about", methods=["GET"])
def about():
    return render_template("main/about.html", title="About")


@main.route("/market", methods=["GET"])
def market():
    return render_template("main/market.html", title="Market", products=products)


@main.route("/market/add", methods=["GET"])
def market_add():
    return render_template("main/market_add.html", title="Add to Market")


@main.route("/market/add", methods=["POST"])
def market_add_post():
    name = request.form.get("name")
    price = request.form.get("price")
    description = request.form.get("description")

    if not name or not price:
        flash("Please fill all fields")
        return redirect(url_for("main.market_add"))

    new_product = Product(name, price, description)
    db.session.add(new_product)
    db.session.commit()

    global products
    products = Product.query.all()

    return redirect(url_for("main.market_add"))
