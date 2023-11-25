"""Top level views for the application."""

from calendar import month_name
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required
from . import main
from .forms import ReservationForm, ReserveSlotForm
from .utils import get_next_month_year, get_reservation_date
from .model_services import (
    create_new_reservation_slots, get_is_admin, get_reservations, update_reservation, get_slot_information,
    get_reservation_so_far
)


@main.route("/")
def index():
    """Renders HTML template for the home page

    Returns
    -------
    flask.Response
        HTML template for the home page
    """
    return render_template("index.html")


@main.route("/reserve", methods=["GET", "POST"])
@login_required
def table_reservation():
    """Main route for the table reservation

    Returns
    -------
    flask.Response
        HTML template for the table reservation
    """
    reservation_date = get_reservation_date(request.args.get("for_date"))

    reservations = get_reservations(reservation_date=reservation_date, user=current_user)

    # TODO: Add a flash message for the user
    res_form = ReservationForm()
    if res_form.validate_on_submit():
        update_reservation(reservations=reservations, slot_reserved_statuses=res_form.slot_reserved_statuses.data)
        return redirect(f"{url_for('main.table_reservation')}?for_date={reservation_date.strftime('%Y-%m-%d')}")

    slot_reserves, slot_reserved_statuses = get_slot_information(reservations)
    res_form = ReservationForm(reserve_date=reservation_date, slot_reserved_statuses=slot_reserved_statuses)

    return render_template("table_reservation/tables.html", res_form=res_form, slot_reserves=slot_reserves)


@main.route("/admin", methods=["GET", "POST"])
@login_required
def admin_reservation():
    """Main route for the admin reservation

    Returns
    -------
    flask.Response
        HTML template for the admin reservation
    """

    is_admin = get_is_admin(current_user)
    if not is_admin:
        return redirect(url_for("main.home"))

    res_so_far_from, res_so_far_to = get_reservation_so_far()
    year, next_month = get_next_month_year(res_so_far_to)

    res_slot_form = ReserveSlotForm()
    if res_slot_form.validate_on_submit():
        create_new_reservation_slots(year, next_month)
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
