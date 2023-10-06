"""error handlers for the main blueprint"""


from flask import render_template
from . import main


@main.app_errorhandler(404)  # 404 is the status code for Not Found error
def page_not_found(e):
    return render_template("404.html"), 404


@main.app_errorhandler(500)  # 500 is the status code for Internal Server Error
def internal_server_error(e):
    return render_template("500.html"), 500
