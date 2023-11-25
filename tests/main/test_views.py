
from unittest.mock import MagicMock, patch
from tests.utils import FlaskAppTestCase
from app import main
from flask import Flask, request
from flask_login import LoginManager, UserMixin


class FlaskIndexViewTestCase(FlaskAppTestCase):

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Stranger" in response.data)



from flask import Flask, request

class MockReservationForm:
    def __init__(self, **kwargs):
        self.reserve_date = kwargs.get("reserve_date")
        self.slot_reserved_statuses = MagicMock()

    def validate_on_submit(self):
        return False  # Return True to test submission logic


import unittest

class TestTableReservation(FlaskAppTestCase):


    def test_table_reservation_view(self):
        self.app.config["LOGIN_DISABLED"] = True
        view_path = "app.main.views"
        with self.app.test_request_context("/reserve"):
            with patch(f"{view_path}.get_reservation_date") as mock_get_date, \
                 patch(f"{view_path}.get_reservations") as mock_get_res, \
                 patch(f"{view_path}.get_slot_information") as mock_get_slot_info, \
                 patch(f"{view_path}.ReservationForm", MockReservationForm):
                mock_get_date.return_value = "2023-11-22"
                mock_get_res.return_value = MagicMock()
                mock_get_slot_info.return_value = (MagicMock(), MagicMock())
                response = main.views.table_reservation()
                
                print (response.data)
                self.assertEqual(response.status_code, 200)
                self.assertIn(b"tables.html", response.data)
                mock_get_date.assert_called_once_with(request.args.get("for_date"))
                mock_get_res.assert_called_once_with(reservation_date="2023-11-22", user=self.current_user)
                mock_get_slot_info.assert_called_once_with(mock_get_res.return_value)
