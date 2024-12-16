from flask import Blueprint, render_template, flash,redirect,request,jsonify
#from .models import Product,Cart,Order
from flask_login import login_required,current_user
from . import db

views=Blueprint('views', __name__)

@views.route('/')
def home():
    #jobs=Jobs.query.filter_by(flash_sale=True)
    return render_template('home.html')



@views.route("/applications")
def applications():
    return render_template("applications.html")

@views.route("/Vacancies")
def vacancies():
    return render_template("Vacancies.html")