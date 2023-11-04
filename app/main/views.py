from flask import render_template, session, redirect, url_for
from .. import db
from ..models import User, Reservation, Table
from . import main
from .forms import NameForm, ReservationForm


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


@main.route("/", methods=["GET", "POST"])
def table_reservation():
    date_form = ReservationForm()
    slots = []
    if date_form.validate_on_submit():
        print(date_form.reserve_date.data)
        session["date"] = date_form.reserve_date.data

        reserve_date = session["date"]

        reservations = Reservation.query.filter_by(reservation_date=reserve_date).all()
        print(reservations)

        slot_tables = []

        for reservation in reservations:
            table_reserved = {}
            table = Table.query.filter_by(id=reservation.table_id).first()

            table_reserved["table_no"] = table.id
            table_reserved["seat_capacity"] = table.table_capacity.value
            table_reserved["reservation_time_slot"] = reservation.reservation_time_slot.name.capitalize()
            table_reserved["reservation_status"] = (
                "Reserved" if reservation.reservation_status else "Not reserved"
            )

            slot_tables.append(table_reserved)
            
        slots = [slot_tables]
        session["slots"] = slots
        return redirect(url_for("main.table_reservation"))

    return render_template(
        "table_reservation/tables.html",
        date_form=date_form,
        slots=session["slots"] if "slots" in session else [],
    )
