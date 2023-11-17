from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms import FieldList
from wtforms.fields import FormField


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


class ReservedForm(FlaskForm):
    reserved = BooleanField("Reserve")


class ReservationForm(FlaskForm):
    reserve_date = DateField("Reserve date", format="%Y-%m-%d")
    slot_reserved_statuses = FieldList(FormField(ReservedForm))
    submit = SubmitField("Reserve Tables")


class ReserveSlotForm(FlaskForm):
    reserve_from_date = DateField("From date", format="%Y-%m-%d")
    reserve_to_date = DateField("To date", format="%Y-%m-%d")
    submit = SubmitField("Create slot tables")


# experiments
class ItemForm(FlaskForm):
    reserved = BooleanField(label="Reserve")


class SelectItemsForm(FlaskForm):
    reserved_items = FieldList(FormField(ItemForm), min_entries=1)
