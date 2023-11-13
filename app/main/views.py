"""Top level views for the application."""

from calendar import monthrange, month_name
from datetime import date
from itertools import product
from dateutil.relativedelta import relativedelta
from flask import render_template, session, redirect, url_for
from flask_login import current_user, login_required
from sqlalchemy import and_, or_ 
from .. import db
from . import main
from .forms import NameForm, ReservationForm, ReserveSlotForm
from ..models import User, Reservation, Table, Role, ReservationSlot



@main.route("/")
@main.route("/home")
def index():
    """Renders HTML template for the home page"""
    return render_template("index.html")


@main.route("/reserve", methods=["GET", "POST"])
@login_required
def table_reservation():
    admin_role = Role.query.filter_by(name="Admin").first()
    is_admin = current_user.role == admin_role

    if not is_admin:
        reservations = Reservation.query.filter(
            and_(
                Reservation.reservation_date == date.today(),
                or_(
                    Reservation.user_id == current_user.id,
                    Reservation.reservation_status == False,
                ),
            )
        ).all()
    else:
        reservations = Reservation.query.filter(
            Reservation.reservation_date == date.today()
        ).all()

    res_form = ReservationForm()
    if res_form.validate_on_submit():
        for idx, reservation in enumerate(reservations):
            reserved_form = res_form.reserved_statuses.data[idx]["reserved"]
            if reservation.reservation_status is not reserved_form:
                reservation.reservation_status = reserved_form
                reservation.user_id = current_user.id if reserved_form else None

        db.session.commit()
        return redirect(url_for("main.table_reservation"))

    slots = []
    slot_tables = []
    reserved_statuses = []
    table_capacities = {
        table.id: table.table_capacity.value for table in Table.query.all()
    }
    users = {user.id: user.username for user in User.query.all()}

    for reservation in reservations:
        table_reserved = {
            "table_no": reservation.table_id,
            "seat_capacity": table_capacities[reservation.table_id],
            "reservation_time_slot": reservation.reservation_time_slot.name.capitalize(),
            "reservation_status": reservation.get_status_string().capitalize(),
            "reserved_by": users[reservation.user_id] if reservation.user_id else "",
        }

        slot_tables.append(table_reserved)
        reserved_statuses.append({"reserved": reservation.reservation_status})

    slots = [slot_tables]
    return render_template(
        "table_reservation/tables.html",
        res_form=ReservationForm(
            reserve_date=date.today(), reserved_statuses=reserved_statuses
        ),
        slots=slots,
    )


def get_reservation_slots(year, month):
    tables = Table.query.all()
    _, num_days = monthrange(year, month)
    days = [date(year, month, day) for day in range(1, num_days + 1)]
    reservation_slots = []
    for date_slot, reservation_slot, table in product(days, ReservationSlot, tables):
        reservation_slots.append(
            Reservation(
                reservation_time_slot=reservation_slot,
                table=table,
                reservation_date=date_slot,
                reservation_status=False,
            )
        )
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
        db.session.add_all(get_reservation_slots(year, next_month))
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
