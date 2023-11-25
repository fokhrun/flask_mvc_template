""" This module contains the forms for the main blueprint """

from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, BooleanField
from wtforms import FieldList
from wtforms.fields import FormField


class ReservedForm(FlaskForm):
    """Reserve form
    
    Parameters
    ----------
        wtforms.FlaskForm
    """
    reserved = BooleanField("Reserve")


class ReservationForm(FlaskForm):
    """Reserve Tables form

    Parameters
    ----------
        wtforms.FlaskForm
    """
    reserve_date = DateField("Reserve date", format="%Y-%m-%d")
    slot_reserved_statuses = FieldList(FormField(ReservedForm))
    submit = SubmitField("Reserve Tables")


class ReserveSlotForm(FlaskForm):
    """Slot tables form

    Parameters
    ----------
        wtforms.FlaskForm
    """
    reserve_from_date = DateField("From date", format="%Y-%m-%d")
    reserve_to_date = DateField("To date", format="%Y-%m-%d")
    submit = SubmitField("Create Reservation Slots")
