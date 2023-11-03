"""Routes of the applications to be in the main blueprint"""


from flask import render_template, session, redirect, url_for
from .. import db
from . import main
from .forms import NameForm
from ..models import User


@main.route("/", methods=["GET", "POST"])
def index():
    """Home page route"""

    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        return redirect(url_for(".index"))  # the endpoint for this route

    return render_template(
        "index.html",
        form=form,
        name=session.get("known", False)
    )
