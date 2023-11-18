import unittest
from app import create_app, db
from app.models import User
from utils import FlaskAppTestCaseWithModels
from app.main.model_services import get_is_admin



class UserModelTestCase(FlaskAppTestCaseWithModels):
    def test_get_is_admin(self):
        admin_user = User.query.filter_by(username="xx").first()
        self.assertTrue(get_is_admin(admin_user))
