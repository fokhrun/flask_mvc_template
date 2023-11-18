"""Top level views for the application."""

from calendar import month_name
from datetime import date, datetime
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from sqlalchemy import and_, or_
from .. import db
from . import main
from .forms import ReservationForm, ReserveSlotForm
from .utils import get_next_month_year, get_reservation_slots
from ..models import User, Reservation, Table, Role


@main.route("/")
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
        new_res = [Reservation(**res) for res in get_reservation_slots(year=year, month=next_month, tables=tables)]
        db.session.add_all(new_res)
        db.session.commit()
        return redirect(url_for("main.admin_reservation"))

    return render_template(
        "table_reservation/admin.html",
        res_slot_form=res_slot_form,
        res_so_far_from=res_so_far_from,
        res_so_far_to=res_so_far_to,
        year=year,
        next_month=month_name[next_month],
        is_admin=is_admin,
    )
