"""Top level views for the application."""

from calendar import monthrange, month_name
from datetime import date
from itertools import product
from dateutil.relativedelta import relativedelta
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from sqlalchemy import and_, or_
from .. import db
from . import main
from .forms import ReservationForm, ReserveSlotForm
from ..models import User, Reservation, Table, Role, ReservationSlot
from datetime import datetime


@main.route("/")
@main.route("/home")
def index():
    """Renders HTML template for the home page"""
    return render_template("index.html")


@main.route("/reserve", methods=["GET", "POST"])
@login_required
def table_reservation():
    for_date = request.args.get("for_date")
    reservation_date = (
        date.today() if for_date == "today" else datetime.strptime(for_date, "%Y-%m-%d")
    )

    admin_role = Role.query.filter_by(name="Admin").first()
    is_admin = current_user.role == admin_role

    if not is_admin:
        reservations = (
            Reservation.query.filter(
                and_(
                    Reservation.reservation_date == reservation_date,
                    or_(
                        Reservation.user_id == current_user.id,
                        Reservation.reservation_status == False,
                    ),
                )
            )
            .order_by(Reservation.reservation_time_slot)
            .all()
        )
    else:
        reservations = (
            Reservation.query.filter(Reservation.reservation_date == reservation_date)
            .order_by(Reservation.reservation_time_slot)
            .all()
        )

    res_form = ReservationForm()
    if res_form.validate_on_submit():
        for idx, reservation in enumerate(reservations):
            reserved_form = res_form.slot_reserved_statuses.data[idx]["reserved"]
            if reservation.reservation_status is not reserved_form:
                reservation.reservation_status = reserved_form
                reservation.user_id = current_user.id if reserved_form else None

        db.session.commit()
        return redirect(url_for("main.table_reservation") +  "".join(["?for_date=", reservation_date.strftime("%Y-%m-%d")]))

    slot_reserves = {}
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
        
        slot_reserved_statuses.append(
                {"reserved": reservation.reservation_status}
            )

    reserve_form = ReservationForm(
        reserve_date=reservation_date, slot_reserved_statuses=slot_reserved_statuses
    )
    return render_template(
        "table_reservation/tables.html",
        res_form=reserve_form,
        slot_reserves=slot_reserves,
    )


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
        list of reservation slots
    """
    _, num_days = monthrange(year, month)
    days = [date(year, month, day) for day in range(1, num_days + 1)]
    reservation_slots = [
        {
            "reservation_slot": reservation_slot,
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


@main.route("/admin", methods=["GET", "POST"])
@login_required
def admin_reservation():
    admin_role = Role.query.filter_by(name="Admin").first()
    is_admin = current_user.role == admin_role
    if not is_admin:
        return redirect(url_for("main.home"))
    res_so_far = sorted(
        list(
            set(
                [
                    reservation.reservation_date
                    for reservation in Reservation.query.filter(
                        Reservation.reservation_date >= date.today()
                    ).all()
                ]
            )
        )
    )

    res_so_far_from, *_, res_so_far_to = res_so_far

    year, next_month = get_next_month_year(res_so_far_to)

    res_slot_form = ReserveSlotForm()
    if res_slot_form.validate_on_submit():
        tables = Table.query.all()
        db.session.add_all(
            [
                Reservation(**res)
                for res in get_reservation_slots(
                    year=year, month=next_month, tables=tables
                )
            ]
        )
        db.session.commit()
        return redirect(url_for("main.admin_reservation"))

    return render_template(
        "admin.html",
        res_slot_form=res_slot_form,
        res_so_far_from=res_so_far_from,
        res_so_far_to=res_so_far_to,
        year=year,
        next_month=month_name[next_month],
        is_admin=is_admin,
    )
