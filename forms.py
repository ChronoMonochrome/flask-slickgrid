from flask_wtf import FlaskForm
from flask_babel import lazy_gettext, gettext, ngettext
from wtforms import PasswordField, Form, FormField, FieldList, HiddenField, SubmitField, IntegerField, StringField, TextAreaField, SelectField, SubmitField, validators, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from widgets import SlickGrid

class TestForm(FlaskForm):
	myGrid = SlickGrid("myGrid", style={"width": "100%", "height": "700px"})
	submit = SubmitField("Save")
	data = HiddenField("data")
