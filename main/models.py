from application import db


class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(120), nullable=True)

    def __init__(self, name, price, description=None):
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        return "<Product %r>" % self.name

    def __str__(self):
        return "Product %r" % self.name
