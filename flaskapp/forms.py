from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class NewContactForm(FlaskForm):
  first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
  last_name = StringField('Last Name',
                          validators=[DataRequired(), Length(min=2, max=20)])
  mail_adress = StringField('Email',
                            validators=[DataRequired(), Email()])
  phone_number = StringField('Phone Number',
                             validators=[DataRequired(), Length(min=2, max=20)])
  phone_number_mobile = StringField('Phone Number Mobile',
                                    validators=[DataRequired(), Length(min=2, max=20)])
  gender = RadioField('Gender', choices=[('OFF', 'Female'), ('OFF', 'Male'), ('OFF', 'Divers')], validators=[DataRequired()])
  submit = SubmitField('Save Contact')


class NewItemForm(FlaskForm):
  name = StringField('Item Name',
                     validators=[DataRequired(), Length(min=2, max=20)])
  typ = StringField('Item Type',
                    validators=[DataRequired(), Length(min=2, max=20)])
  status = RadioField('Status', choices=[('In Storage'), ('In Repair'), ('Rent Out')])
  location = StringField('Location',
                         validators=[DataRequired(), Length(min=2, max=20)])
  price = StringField('Price',
                      validators=[DataRequired(), Length(min=2, max=20)])
  submit = SubmitField('Save Item')