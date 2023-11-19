
from tests.utils import FlaskAppTestCaseWithModels
from app.models import User, ReservationSlot
from app.main.model_services import get_is_admin, get_reservations


class UserModelTestCase(FlaskAppTestCaseWithModels):
    def test_get_is_admin(self):
        self.assertTrue(get_is_admin(User.query.filter_by(username="xx").first()))
        self.assertFalse(get_is_admin(User.query.filter_by(username="xy").first()))


class ReservationModelTestCase(FlaskAppTestCaseWithModels):

    expected_slots = {ReservationSlot.evening.name, ReservationSlot.night.name}

    def get_reservation_information(self, user, date):
        reservations = get_reservations(
            is_admin=get_is_admin(user),
            reservation_date=date,
            current_user=user
        )

        count = len(reservations)
        slots = {_.reservation_time_slot.name for _ in reservations}
        users = {_.user_id for _ in reservations}
        dates = {_.reservation_date for _ in reservations}
        statuses = {_.reservation_status for _ in reservations}

        return count, slots, users, dates, statuses

    def test_get_reservations_admin(self):
        user = User.query.filter_by(username="xx").first()
        res_date = self.reservation_date_1
        count, slots, users, dates, status = self.get_reservation_information(user=user,
                                                                              date=res_date)

        self.assertEqual(count, 2)
        self.assertEqual(slots, self.expected_slots)
        self.assertEqual(dates, {res_date})
        self.assertTrue(status.pop())
        self.assertTrue(user.id in users)
    
    def test_get_reservations(self):
        user = User.query.filter_by(username="xy").first()
        res_date = self.reservation_date_1
        count, slots, users, dates, status = self.get_reservation_information(user=user,
                                                                              date=res_date)

        self.assertEqual(count, 1)
        self.assertTrue(status.pop())
        self.assertEqual(slots.pop(), ReservationSlot.night.name)
        self.assertEqual(dates, {res_date})
        self.assertTrue(users, {user.id})
    
    def test_get_reservations_reserved(self):
        user = User.query.filter_by(username="xy").first()
        res_date = self.reservation_date_2
        count, slots, users, dates, status = self.get_reservation_information(user=user,
                                                                              date=res_date)
        self.assertEqual(count, 1)
        self.assertFalse(status.pop())
        self.assertEqual(slots, {ReservationSlot.night.name})
        self.assertEqual(dates, {res_date})
        self.assertTrue(users, {user.id})

    def test_get_reservations_unreserved(self):
        user = User.query.filter_by(username="xy").first()
        res_date = self.reservation_date_3
        count, slots, users, dates, status = self.get_reservation_information(user=user,
                                                                              date=res_date)

        self.assertEqual(count, 2)
        self.assertFalse(status.pop())
        self.assertEqual(slots, self.expected_slots)
        self.assertEqual(dates, {res_date})
        self.assertTrue(users, {user.id})
