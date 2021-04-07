from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    # flaskforms checks the form fields based on the name of the function.
    # So, here, it'll know that this function is linked to the username field.
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                'Username already exists. Please, try a different one.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError(
                'Email address already exists. Please, try a different one.')

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


class LoginForm(FlaskForm):
    username = StringField(label='Username :', validators=[DataRequired()])
    password = PasswordField(label='Password :', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')