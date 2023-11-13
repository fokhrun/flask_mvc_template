"""
App entry point.
1. Run flask app --> flask run
1.1. Run flask app with debug --> flask run --debug
1.2. Run flask app with "development" environment --> FLASK_CONFIG=development flask run
1.3 Run flask tests --> flask test
"""

import os
import unittest
import click
from coverage import coverage as test_coverage
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role


app = create_app(os.getenv("FLASK_CONFIG"))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    """Add objects to the shell context for flask shell command"""
    return {"db": db, "User": User, "Role": Role}


@app.cli.command()
@click.argument("test_names", nargs=-1)
def test(test_names):
    """Run unit tests with test coverage

    Parameters
    ----------
    cover : bool
        enable calculating test coverage
    test_names : str
        specific test to run
    """
    cov = None  # coverage object
    if os.environ.get("FLASK_TEST_COVERAGE"):  # if FLASK_TEST_COVERAGE is set to 1
        cov = test_coverage(branch=True, include="app/*")   # coverage area is app/
        cov.start()

    # run tests with full scope or specific test
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)  # load specific test
    else:
        tests = unittest.TestLoader().discover("tests")  # load all tests
    unittest.TextTestRunner(verbosity=2).run(tests)  # run tests

    if cov:
        cov.stop()
        cov.save()
        print("Coverage Summary:")
        cov.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, "tmp", "coverage")
        cov.html_report(directory=covdir)
        cov.erase()
