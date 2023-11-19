
from tests.utils import FlaskAppTestCaseWithModels
from app.models import User, ReservationSlot
from app.main.model_services import get_is_admin, get_slot_information, get_reservations, update_reservation


class UserModelTestCase(FlaskAppTestCaseWithModels):
    def test_get_is_admin(self):
        self.assertTrue(get_is_admin(User.query.filter_by(username="xx").first()))
        self.assertFalse(get_is_admin(User.query.filter_by(username="xy").first()))


class ReservationModelTestCase(FlaskAppTestCaseWithModels):

    expected_slots = {ReservationSlot.evening.name, ReservationSlot.night.name}

    def get_reservation_information(self, user, date):
        reservations = get_reservations(reservation_date=date, user=user)
        count = len(reservations)
        slots = {_.reservation_time_slot.name for _ in reservations}
        users = {_.user_id for _ in reservations}
        dates = {_.reservation_date for _ in reservations}
        statuses = {_.reservation_status for _ in reservations}

        return count, slots, users, dates, statuses

    def test_get_reservations_admin(self):
        user = User.query.filter_by(username="xx").first()
        res_date = self.reservation_date_1
        count, slots, users, dates, statuses = self.get_reservation_information(user=user, date=res_date)

        self.assertEqual(count, 2)
        self.assertEqual(slots, self.expected_slots)
        self.assertEqual(dates, {res_date})
        self.assertTrue(statuses.pop())
        self.assertTrue(user.id in users)

    def test_get_reservations(self):
        user = User.query.filter_by(username="xy").first()
        res_date = self.reservation_date_1
        count, slots, users, dates, statuses = self.get_reservation_information(user=user, date=res_date)

        self.assertEqual(count, 1)
        self.assertTrue(statuses.pop())
        self.assertEqual(slots.pop(), ReservationSlot.night.name)
        self.assertEqual(dates, {res_date})
        self.assertTrue(users, {user.id})

    def test_get_reservations_reserved(self):
        user = User.query.filter_by(username="xy").first()
        res_date = self.reservation_date_2
        count, slots, users, dates, statuses = self.get_reservation_information(user=user, date=res_date)
        self.assertEqual(count, 1)
        self.assertFalse(statuses.pop())
        self.assertEqual(slots, {ReservationSlot.night.name})
        self.assertEqual(dates, {res_date})
        self.assertTrue(users, {user.id})

    def test_get_reservations_unreserved(self):
        user = User.query.filter_by(username="xy").first()
        res_date = self.reservation_date_3
        count, slots, users, dates, statuses = self.get_reservation_information(user=user, date=res_date)

        self.assertEqual(count, 2)
        self.assertFalse(statuses.pop())
        self.assertEqual(slots, self.expected_slots)
        self.assertEqual(dates, {res_date})
        self.assertTrue(users, {user.id})


class ReservationModelUpdateTestCase(FlaskAppTestCaseWithModels):

    def test_update_reservation(self):
        user = User.query.filter_by(username="xy").first()
        res_date = self.reservation_date_1
        update_reservation(
            reservations=get_reservations(reservation_date=res_date, user=user),
            slot_reserved_statuses=[{'reserved': False}]
        )
        res = get_reservations(reservation_date=res_date, user=user)
        self.assertEqual(len(res), 1)
        self.assertFalse({_.reservation_status for _ in res}.pop())


class ReservationModelStatusTestCast(FlaskAppTestCaseWithModels):

    def test_get_slot_information(self):
        user = User.query.filter_by(username="xx").first()
        res_date = self.reservation_date_1
        reservations = get_reservations(reservation_date=res_date, user=user)
        slot_reserves, slot_reserved_statuses = get_slot_information(reservations)
        self.assertEqual(
            {_ for _ in slot_reserves}, 
            {ReservationSlot.evening.name.capitalize(), ReservationSlot.night.name.capitalize()}
        )
        for _ in slot_reserves.values():
            self.assertEqual(len(_), 1)
        self.assertEqual(
            [_["reserved"] for _ in slot_reserved_statuses],
            [_.reservation_status for _ in reservations]
        )
