from flask import Blueprint, render_template, flash, send_from_directory, redirect
from flask_login import login_required, current_user
from .forms import VacancyForm
from werkzeug.utils import secure_filename
from .models import Vacancy
from . import db

admin=Blueprint('admin', __name__)

#this is for viewing the file images fetched from the db
@admin.route('/media/<path:filename>')   
def get_image(filename):
    return send_from_directory('../media', filename)

#Adding the vacancy details to the db
@admin.route('/add-vacancy', methods=['POST','GET'])
@login_required
def add_vacancy():
    if current_user.id==1:
        form=VacancyForm()
        if form.validate_on_submit():
            title = form.title.data
            department = form.department.data
            contract_type=form.contract_type.data
            posted_date=form.expiry_date.data
            expiry_date=form.expiry_date.data
            description=form.description.data

            #file=form.product_picture.data
            #file_name=secure_filename(file.filename) #this removes whitespaces and invallid characters from filename

            #file_path = f'./media/{file_name}'

            #file.save(file_path)

            new_vacancy=Vacancy()
            new_vacancy.title=title
            new_vacancy.department=department
            new_vacancy.contract_type=contract_type
            new_vacancy.posted_date=posted_date
            new_vacancy.expiry_date=expiry_date
            new_vacancy.description=description

           # new_vacancy.product_picture=file_path

            try:
                db.session.add(new_vacancy)
                db.session.commit()
                flash(f'{title}, Added Successfully')

                return render_template('add-vacancy.html', form=form)

            except Exception as e:
                print(e)
                flash('Vacancy not added')

        return render_template('/add-vacancy.html', form=form)
    return render_template('404.html')