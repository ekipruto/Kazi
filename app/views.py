from flask import Blueprint, render_template, flash,redirect,request,jsonify
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

@views.route('/profile', methods=['GET, POST'])
@login_required
def profile():
    form=ProfileForm()
    if form.validate_on_submit():
        email=form.email.data
        title=form.title.data
        first_name=form.first_name.data
        last_name=form.last_name.data
        gender=form.gender.data
        dob=form.dob.data
        phone=form.phone.data
        alt_phone=form.alt_phone.data
        postal_address=form.postal_address.data
        postal_code=form.postal_code.data

        user_profile=Profile()
        user_profile.email=email
        user_profile.title=title
        user_profile.first_name=first_name
        user_profile.last_name=last_name
        user_profile.gender=gender
        user_profile.dob=dob
        user_profile.phone=phone
        user_profile.alt_phone=alt_phone
        user_profile.postal_address=postal_address
        user_profile.postal_code=postal_code
        
        try:
            db.session.add(user_profile)
            db.session.commit()
            flash('records added successfully')
            return redirect('/profile')
            
        except Exception as e:
            print(e)
            flash('Profile not created, try again')

            form.email.data=''
            form.title.data=''
            form.first_name.data-=''
            form.last_name.data=''
            form.gender.data=''
            form.dob.data=''
            form.phone.data-=''
            form.alt_phone.data=''
            form.postal_address.data=''
            form.postal_code.data-=''
    return render_template('profile.html', form=form)