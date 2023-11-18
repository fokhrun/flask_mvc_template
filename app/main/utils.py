"""Utility functions for the admin routes"""

from datetime import date
from itertools import product
from calendar import monthrange
from dateutil.relativedelta import relativedelta
from ..models import ReservationSlot


def get_reservation_slots(year, month, tables):
    """Generate reservation slots for a given month and year

    Parameters
    ----------
    tables : list[Table]
    year : int
    month : int

    Returns
    -------
    list[dict]
        reservation slots
    """
    _, num_days = monthrange(year, month)
    days = [date(year, month, day) for day in range(1, num_days + 1)]
    reservation_slots = [
        {
            "reservation_time_slot": reservation_slot,
            "table": table,
            "reservation_date": date_slot,
            "reservation_status": False,
        }
        for date_slot, reservation_slot, table in product(days, ReservationSlot, tables)
    ]

    return reservation_slots


def get_next_month_year(current_date):
    """Calculate next month and year from a given date

    Parameters
    ----------
    current_date : datetime.date

    Returns
    -------
        next_year : int
        next_month : int
    """
    next_month_date = current_date + relativedelta(months=1)
    next_month = next_month_date.month
    next_year = next_month_date.year
    return next_year, next_month
