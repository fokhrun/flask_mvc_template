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
    reserved_statuses = FieldList(FormField(ReservedForm))
    submit = SubmitField("Reserve Tables")


class ItemForm(FlaskForm):
    reserved = BooleanField(label="Reserve")


class SelectItemsForm(FlaskForm):
    reserved_items = FieldList(FormField(ItemForm), min_entries=1)
