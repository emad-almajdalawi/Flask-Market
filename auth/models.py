from application import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# UserMixin is a class that Flask-Login uses to create is_authenticated(), is_active(), is_anonymous(), and get_id() methods
class User(db.Model, UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    products = db.relationship("Product", backref="owned", lazy=True)

    @property
    def hashed_password(self):
        return self.password

    @hashed_password.setter
    def hashed_password(self, the_password):
        self.password = bcrypt.generate_password_hash(the_password).decode("utf-8")

    def check_password(self, the_password):
        return bcrypt.check_password_hash(self.password, the_password)

    def __init__(self, username, email, hashed_password):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password

    def __repr__(self):
        return "<User %r>" % self.username

    def __str__(self):
        return "User %r" % self.username
