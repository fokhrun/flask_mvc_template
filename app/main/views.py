"""Routes of the applications to be in the main blueprint"""


from datetime import datetime
from flask import render_template, session
from . import main


@main.route("/", methods=["GET", "POST"])
def index():
    """Home page route"""
    return render_template(
        "index.html",
        name=session.get("known", False),
        current_time=datetime.utcnow()
    )
