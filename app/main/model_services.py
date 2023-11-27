"""Service that handles all the business logic that uses the models"""

from collections import OrderedDict
from sqlalchemy import and_, or_
from flask_login import current_user
from .. import db
from ..models import User, Reservation, Table, Role
from .utils import get_reservation_slots


def get_is_admin(active_user):
    """
    Get if active user is admin

    Parameters
    ----------
    active_user : User
        Active user in the app

    Returns
    -------
        bool
    """
    admin_role = Role.query.filter_by(name="Admin").first()
    is_admin = active_user.role == admin_role

    return is_admin


def get_reservations(reservation_date, user):
    """
    Get reservations for a user or admin under for a given date for certain conditions

    Parameters
    ----------
    reservation_date : date
        Date for which reservations are to be fetched
    user : User
        Active user in the app

    Returns
    -------
        list[Reservation]
    """
    if get_is_admin(user):
        reservations = Reservation.query.filter(
            Reservation.reservation_date == reservation_date
        )
    else:
        get_non_reserved_today = and_(
            Reservation.reservation_date == reservation_date,
            or_(
                Reservation.user_id == user.id,
                # pylint: disable=C0121
                Reservation.reservation_status == False
            ),
        )
        reservations = Reservation.query.filter(get_non_reserved_today)

    reservation_sorted = reservations.order_by(Reservation.reservation_time_slot).all()

    return reservation_sorted


def update_reservation(reservations, slot_reserved_statuses):
    """Update reservation status for a given list of reservations

    Parameters
    ----------
    reservations : list[Reservation]
    slot_reserved_statuses : list[dict]

    Returns
    -------
        bool
        True if reservation is updated, False otherwise
    """
    for idx, reservation in enumerate(reservations):
        reserved_form = slot_reserved_statuses[idx]['reserved']
        if reservation.reservation_status is not reserved_form:
            reservation.reservation_status = reserved_form
            reservation.user_id = current_user.id if reserved_form else None

    db.session.commit()


def get_slot_information(reservations):
    """_summary_

    Parameters
    ----------
    reservations : list[Reservation]


    Returns
    -------
        tuple
        slot_reserves : dict
            Dictionary of reservations for a given time slot
        slot_reserved_statuses : list[dict]
            List of reservation statuses for a given time slot
    """
    slot_reserves = OrderedDict()
    slot_reserved_statuses = []
    table_capacities = {
        table.id: table.table_capacity.value for table in Table.query.all()
    }
    users = {user.id: user.username for user in User.query.all()}

    for reservation in reservations:
        reservation_time_slot = reservation.reservation_time_slot.name.capitalize()
        table_reserved = {
            "table_no": reservation.table_id,
            "seat_capacity": table_capacities[reservation.table_id],
            "reservation_time_slot": reservation_time_slot,
            "reservation_status": reservation.get_status_string().capitalize(),
            "reserved_by": users[reservation.user_id] if reservation.user_id else "",
        }

        if reservation_time_slot in slot_reserves:
            slot_reserves[reservation_time_slot].append(table_reserved)
        else:
            slot_reserves[reservation_time_slot] = [table_reserved]

        slot_reserved_statuses.append({"reserved": reservation.reservation_status})

    return slot_reserves, slot_reserved_statuses


def get_reservation_so_far():
    """Get reservation date range for the admin reservation

    Returns
    -------
        tuple(datetime.date, datetime.date)
    """
    res_so_far_from = (
        Reservation.query.order_by(Reservation.reservation_date)
        .first()
        .reservation_date
    )
    res_so_far_to = (
        Reservation.query.order_by(Reservation.reservation_date.desc())
        .first()
        .reservation_date
    )

    return res_so_far_from, res_so_far_to


def create_new_reservation_slots(year, next_month):
    """Create new reservation slots for the next month

    Parameters
    ----------
    year : int
    next_month : int
    """
    db.session.add_all(
        [
            Reservation(**res)
            for res in get_reservation_slots(
                year=year, month=next_month, tables=Table.query.all()
            )
        ]
    )
    db.session.commit()
