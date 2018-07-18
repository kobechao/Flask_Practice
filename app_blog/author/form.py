from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField
from wtforms.fields.html5 import EmailField

from app_blog.author.model import UserRegister

class FormRegister(Form):

    username = StringField('UserName', validators=[
        validators.DataRequired(),
        validators.Length(4, 30)
    ])
    email = EmailField('Email', validators=[
        validators.DataRequired(),
        validators.Length(1, 50),
        validators.Email()
    ])
    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(2, 10),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Register New Account')

    def validate_email( self, filed ):
        if UserRegister.query.filter_by( email=filed.data ).first():
            raise ValidationError('Email already register by somebody')

    def validate_username( self, filed ):
        if UserRegister.query.filter_by( username=filed.data ).first() :
            raise ValidationError('UserName already register by somebody')

