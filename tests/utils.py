"""Flask login client tests."""

import unittest
from app import create_app, db
from app.models import Role, User


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class FlaskAppTestCaseWithModels(FlaskAppTestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

        admin_role = Role(name="Admin")
        guest_role = Role(name="Guest")

        xx_user = User(username="xx", role=admin_role, email="xx@email.com", password="xxabc")
        xy_user = User(username="xy", role=guest_role, email="xy@email.com", password="xyabc")

        db.session.add_all([admin_role, guest_role, xx_user, xy_user])
        db.session.commit()
