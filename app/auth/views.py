""" This module contains the views for the authentication blueprint. """
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Route for the login page

    Parameters
    ----------
        form : LoginForm
            Form for the login page
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next_args = request.args.get("next")
            if next_args is None or not next_args.startswith("/"):
                next_args = url_for("main.index")
            return redirect(next_args)
        flash("Invalid email or password.")
    return render_template("auth/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    """
    Route for the logout page

    Returns
    -------
        flask.Response
            Redirects to the home page
    """
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    Route for the register page

    Returns
    -------
        flask.Response
            HTML template for the register page
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data.lower(),
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You can now login.")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", form=form)
