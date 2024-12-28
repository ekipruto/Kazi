from flask_wtf import FlaskForm
from wtforms import IntegerField, EmailField, StringField, PasswordField,SubmitField,SelectField,DateField
from wtforms.validators import length,DataRequired,NumberRange,Email
from flask_wtf.file import FileField, FileRequired

class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), length(min=2)])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), length(min=6)])
    password2 = PasswordField('Confirm Your Password', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email=EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Enter Your Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), length(min=6)])
    change_password = SubmitField('Change Password')

class VacancyForm(FlaskForm):
    title = StringField('Name of Vacancy', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    contract_type=StringField('Type of the Contract', validators=[DataRequired()])
    expiry_date=DateField('Job posting date', validators=[DataRequired()])
    expiry_date=DateField('Job expiry date', validators=[DataRequired()])
    description=StringField('Description of the job', validators=[DataRequired()])

    add_vacancy = SubmitField('Add Vacancy')
    update_vacancy = SubmitField('Update')

class ProfileForm(FlaskForm):
   email = StringField('E-mail', validators=[DataRequired(), Email()], render_kw={"readonly": True})
   title = SelectField('Title', choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], validators=[DataRequired()])
   first_name = StringField('First Name', validators=[DataRequired()])
   last_name = StringField('Last Name', validators=[DataRequired()])
   gender = SelectField('Gender', choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
   dob = DateField('Date of Birth', validators=[DataRequired()])
   phone = StringField('Phone', validators=[DataRequired()]) 
   alt_phone = StringField('Alternative Phone')
   postal_address = StringField('Postal Address', validators=[DataRequired()])
   postal_code = StringField('Postal Code', validators=[DataRequired()])