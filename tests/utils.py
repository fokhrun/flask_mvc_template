"""Flask login client tests."""

import unittest
from datetime import date
from app import create_app, db
from app.models import Role, User, ReservationSlot, Table, Reservation


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
        table = Table(table_capacity="two")
        self.reservation_date_1 = date(2023, 11, 1)
        self.reservation_date_2 = date(2023, 11, 2)
        self.reservation_date_3 = date(2023, 11, 3)

        db.session.add_all([admin_role, guest_role, xx_user, xy_user, table])

        db.session.commit()

        db.session.add(
            Reservation(
                reservation_time_slot=ReservationSlot.evening,
                table=table,
                reservation_date=self.reservation_date_1,
                reservation_status=True,
                user_id=xx_user.id,
            )
        )

        db.session.add(
            Reservation(
                reservation_time_slot=ReservationSlot.night,
                table=table,
                reservation_date=self.reservation_date_1,
                reservation_status=True,
                user_id=xy_user.id
            )
        )

        db.session.add(
                Reservation(
                    reservation_time_slot=ReservationSlot.evening,
                    table=table,
                    reservation_date=self.reservation_date_2,
                    reservation_status=True,
                    user_id=xx_user.id
                )
            )

        db.session.add(
            Reservation(
                reservation_time_slot=ReservationSlot.night,
                table=table,
                reservation_date=self.reservation_date_2,
                reservation_status=False
            )
        )

        db.session.add(
                Reservation(
                    reservation_time_slot=ReservationSlot.evening,
                    table=table,
                    reservation_date=self.reservation_date_3,
                    reservation_status=False,
                )
            )

        db.session.add(
            Reservation(
                reservation_time_slot=ReservationSlot.night,
                table=table,
                reservation_date=self.reservation_date_3,
                reservation_status=False
            )
        )

        db.session.commit()
