
import unittest
from unittest import mock
from datetime import date
from app.main.views import get_next_month_year, get_reservation_slots


class TestViewUtils(unittest.TestCase):
    def test_get_next_month_year(self):
        self.assertEqual(get_next_month_year(date(2020, 1, 1)), (2020, 2))
        self.assertEqual(get_next_month_year(date(2020, 12, 1)), (2021, 1))

    def test_get_reservation_slots(self):
        tables = [mock.Mock(), mock.Mock()]
        reservation_slots = get_reservation_slots(year=2020, month=1, tables=tables)
        self.assertTrue(len(reservation_slots), 120)
        self.assertTrue(reservation_slots[0].keys(),
                        ["reservation_slot", "table", "reservation_date", "reservation_status"])
