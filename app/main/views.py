from flask import render_template, session, redirect, url_for
from flask_login import login_required
from .. import db
from ..models import User, Reservation, Table, Role
from . import main
from .forms import NameForm, ReservationForm
from datetime import date
from flask_login import current_user
from sqlalchemy import or_, and_


@main.route("/", methods=["GET", "POST"])
@main.route("/home", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = form.name.data
        return redirect(url_for(".index"))
    return render_template(
        "index.html",
        form=form,
        name=session.get("name"),
        known=session.get("known", False),
    )


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
