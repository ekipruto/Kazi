from flask import Blueprint, render_template, flash,redirect,request,jsonify,url_for
from .models import Vacancy, Profile
#from models import db, Vacancy
from flask_login import login_required,current_user
from datetime import date
from . import db
from . forms import ProfileForm

views=Blueprint('views', __name__)

@views.route('/')
def home():
    #jobs=Jobs.query.filter_by(flash_sale=True)
    return render_template('home.html')



@views.route("/applications")
def applications():
    return render_template("applications.html")

@views.route("/Vacancies")
def list_vacancies():
    vacancies=Vacancy.query.all()
    return render_template("Vacancies.html", vacancies=vacancies)

@views.route('/vacancy/<int:vacancy_id>')
def vacancy_details(vacancy_id):
    vacancy=Vacancy.query.get_or_404(vacancy_id)
    return render_template('vacancy_details.html', vacancy=vacancy)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        email = form.email.data
        title = form.title.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        gender = form.gender.data
        dob = form.dob.data
        phone = form.phone.data
        alt_phone = form.alt_phone.data
        postal_address = form.postal_address.data
        postal_code = form.postal_code.data

        # Check for duplicate email 
        existing_profile = Profile.query.filter_by(email=email).first() 
        if existing_profile: 
           flash(f'A profile with this email already exists. Please use a different email.') 
           return render_template('profile.html', form=form)
        
        user_profile = Profile(
            email=email,
            title=title,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            dob=dob,
            phone=phone,
            alt_phone=alt_phone,
            postal_address=postal_address,
            postal_code=postal_code
        )
        
        try:
            db.session.add(user_profile)
            db.session.commit()
            flash(f'Records added successfully')
            return redirect(url_for('profile'))
        except Exception as e:
            print(e)
            flash(f'Profile not created, try again')
            form = ProfileForm()  # Reset/clear form fields
    
    return render_template('profile.html', form=form)
