"""error handlers"""
# pylint: disable=W0613

from flask import render_template
from . import main


@main.app_errorhandler(404)  # 404 is the status code for Not Found error
def page_not_found(err):
    """Renders HTML template for the 404 page

    Parameters
    ----------
    err : werkzeug.exceptions.NotFound
        error raised when a resource is not found

    Returns
    -------
    flask.Response
        HTML template for the 404 page
    """
    return render_template("404.html"), 404


@main.app_errorhandler(500)  # 500 is the status code for Internal Server Error
def internal_server_error(err):
    """Renders HTML template for the 500 page

    Parameters
    ----------
    err : werkzeug.exceptions.InternalServerError 
        error raised when an internal server error occurs

    Returns
    -------
    flask.Response
        HTML template for the 500 page
    """
    return render_template("500.html"), 500
