
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()


def create_app(config_name="default"):
    """
    Application factory function that delay the creation of the application
    Typically invoked from a script that gives time to set the configuration, 
    and can create multiple application instances. 
    Can be very useful during testing.

    Parameters
    ----------
    config_name : str, optional
        to choose the appropriate configuration, by default "default"

    Returns
    -------
    flask.Flask
        Flask application instance
    """
    from .main import main as main_blueprint
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_blueprint)
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    return app
