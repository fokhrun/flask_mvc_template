
from sqlalchemy import and_, or_
from ..models import User, Reservation, Table, Role


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


def get_reservations(is_admin, reservation_date, current_user):
    """ 
    Get reservations for a user or admin under for a given date for certain conditions

    Parameters
    ----------
    is_admin : bool
        If the user is admin
    reservation_date : date
        Date for which reservations are to be fetched
    current_user : User
        Active user in the app

    Returns
    -------
        list[Reservation]
    """
    if is_admin:
        reservations = Reservation.query.filter(Reservation.reservation_date == reservation_date)
    else:
        get_non_reserved_today = and_(
            Reservation.reservation_date == reservation_date,
            or_(
                Reservation.user_id == current_user.id,
                Reservation.reservation_status == False
                )
            )
        reservations = Reservation.query.filter(get_non_reserved_today)

    reservation_sorted = reservations.order_by(Reservation.reservation_time_slot).all()

    return reservation_sorted
