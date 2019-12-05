# Sources:
# https://www.youtube.com/watch?v=UIJKdCIEXUQ


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class NewProperty(FlaskForm):
    propertyId = IntegerField('Property ID', )


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
     
    def validate_username(self, username):
        query = "SELECT id FROM user WHERE username = '" + username.data + "'" 
        


class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
