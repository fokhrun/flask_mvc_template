"""Basic forms for the main blueprint."""


from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, StringField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    """Form to get the user name"""

    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


class ReservationForm(FlaskForm):
    reserve_date = DateField('reserve_date', format='%Y-%m-%d')
    submit = SubmitField('Show Tables')
