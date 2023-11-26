""" This file is the application package constructor"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


db = SQLAlchemy()  # Database object
login_manager = LoginManager()  # Login manager object
login_manager.login_view = 'auth.login'  # Set the login view


def create_app(config_name):
    """Create an application instance

    Parameters
    ----------
    config_name : str
        Name of the configuration to use

    Returns
    -------
    app : Flask
        The application instance
    """
    app = Flask(__name__)  # Create a new application instance
    app.config.from_object(config[config_name])  # Load the configuration
    config[config_name].init_app(app)  # Initialize the application with the configuration values

    db.init_app(app)  # Initialize the database object with app context
    login_manager.init_app(app)  # Initialize the login manager object with app context

    from .main import main as main_blueprint  # noqa: E402
    app.register_blueprint(main_blueprint)  # Register the routes in main/views.py

    from .auth import auth as auth_blueprint  # noqa: E402
    app.register_blueprint(auth_blueprint, url_prefix="/auth")  # Register the routes in auth/views.py

    return app
