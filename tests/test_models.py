
from app import db
from app.models import User, Role, Table, Reservation, ReservationSlot, TableCapacity
from tests.utils import FlaskAppTestCase
from datetime import date


class UserModelTestCase(FlaskAppTestCase):

    def test_role(self):
        role_xyz = Role(name="xyz")
        user = User(username="xx_yy_zz", role=role_xyz)
        db.session.add(role_xyz)
        db.session.commit()
        user_fetched = user.query.filter(User.role == role_xyz).first()
        self.assertTrue(user_fetched.username == "xx_yy_zz")

    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_seat_capacity(self):
        self.assertTrue(TableCapacity.two.value == 2)
        self.assertTrue(TableCapacity.four.value == 4)
        self.assertTrue(TableCapacity.six.value == 6)
        self.assertRaises(ValueError, TableCapacity, 'seven')

    def test_reservation_string(self):
        reservation = Reservation(
            table=Table(table_capacity=TableCapacity.two),
            reservation_date=date(2023, 11, 1),
            reservation_time_slot=ReservationSlot.evening,
            reservation_status=True,
            user_id=1
        )

        self.assertEqual(reservation.get_status_string(), "reserved")
        reservation.reservation_status = False
        self.assertEqual(reservation.get_status_string(), "unreserved")
