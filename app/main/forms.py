"""Basic forms for the main blueprint."""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    """Form to get the user name"""

    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
