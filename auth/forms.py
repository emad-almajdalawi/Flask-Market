from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField


class SignupForm(FlaskForm):
    username = StringField("Username")
    email = EmailField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Signup")


class LoginForm(FlaskForm):
    email = EmailField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Login")
