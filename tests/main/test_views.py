
import unittest
from datetime import date
from app.main.views import get_next_month_year


class TestViewUtils(unittest.TestCase):
    def test_get_next_month_year(self):
        self.assertEqual(get_next_month_year(date(2020, 1, 1)), (2020, 2))
        self.assertEqual(get_next_month_year(date(2020, 12, 1)), (2021, 1))


