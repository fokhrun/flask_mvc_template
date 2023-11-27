""" Main blueprint. """

# pylint: disable=C0413, R0401

from flask import Blueprint


main = Blueprint("main", __name__)

from . import views, errors
