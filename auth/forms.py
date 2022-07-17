from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, BooleanField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from auth.models import User


class SignupForm(FlaskForm):
    def validate_email(self, check_email):
        user_email = User.query.filter_by(email=check_email.data).first()
        if user_email:
            raise ValidationError("Email already exists")

    def validate_username(self, check_username):
        user_name = User.query.filter_by(username=check_username.data).first()
        if user_name:
            raise ValidationError("Username already exists")

    username = StringField("Username", validators=[Length(min=3, max=20)])
    email = EmailField("Email")
    password = PasswordField("Password", validators=[Length(min=5, max=20)])
    password2 = PasswordField(
        "Repeat Password", validators=[EqualTo("password"), DataRequired()]
    )
    seller = BooleanField("Seller", default=False)
    submit = SubmitField("Signup")


class LoginForm(FlaskForm):
    username = StringField("User Name")
    password = PasswordField("Password")
    submit = SubmitField("Login")
