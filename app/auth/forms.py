"""This module contains the forms for the authentication blueprint."""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    """Form for users to login."""
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log In")


class RegistrationForm(FlaskForm):
    """Form for users to create new account"""
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(
        "Username",
        validators=[
            DataRequired(), Length(1, 64),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                   'Usernames must have only letters, numbers, dots or '
                   'underscores')])
    password = PasswordField(
        "Password",
        validators=[DataRequired(), EqualTo("password2", message="Passwords must match.")]
    )
    password2 = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, field):
        """Validate if email is already registered"""
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError("Email already registered.")

    def validate_username(self, field):
        """Validate if username is already in use"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use.")
