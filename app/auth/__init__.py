""" Auth blueprint. """

from flask import Blueprint

# pylint: disable=C0413, R0401

auth = Blueprint("auth", __name__)


from . import views  # noqa: E402, F401
