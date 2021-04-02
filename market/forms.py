from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='Username :',
                           validators=[Length(min=2, max=30),
                                       DataRequired()])
    email_address = StringField(label='Email Address :',
                                validators=[Email(), DataRequired()])
    password1 = PasswordField(
        label='Password :', validators=[Length(min=8, max=60),
                                        DataRequired()])
    password2 = PasswordField(
        label='Verify Password :',
        validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')
