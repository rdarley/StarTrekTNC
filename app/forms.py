from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    anonymous = BooleanField('Anonymous Hail')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    hail = TextAreaField('Hail', validators=[DataRequired()])
    prime_corrective = BooleanField('Prime Corrective')
    submit = SubmitField('Send Via Subspace')
