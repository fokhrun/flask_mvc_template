
import unittest
from datetime import date
from app.main.views import get_next_month_year
from app import create_app, db


class TestViewUtils(unittest.TestCase):
    def test_get_next_month_year(self):
        self.assertEqual(get_next_month_year(date(2020, 1, 1)), (2020, 2))
        self.assertEqual(get_next_month_year(date(2020, 12, 1)), (2021, 1))


class FlaskIndexViewTestCase(unittest.TestCase):
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

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Stranger" in response.data)
