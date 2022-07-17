from application import db


class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    owner = db.Column(db.Integer(), db.ForeignKey("User.id"), nullable=True)

    def __init__(self, title, price, description=None, owner=None):
        self.title = title
        self.price = price
        self.description = description
        self.owner = owner

    def __repr__(self):
        return "<Product %r>" % self.title

    def __str__(self):
        return "Product %r" % self.title
