from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import date


db = SQLAlchemy()
DB_NAME = 'database.sqlite3'


def create_database():
    db.create_all()
    print('Database Created')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ekipruto'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    #keeping track of the logged in users
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    from .views import views
    from .auth import auth
    #from .admin import admin
    from .models import Users,Vacancy #Cart, Product, Order

    app.register_blueprint(views, url_prefix='/') # localhost:5000/about-us
    app.register_blueprint(auth, url_prefix='/') # localhost:5000/auth/change-password
    #app.register_blueprint(admin, url_prefix='/')

    with app.app_context():
        create_database()
    
    # Dummy data (insert only if empty)
    with app.app_context():
        if Vacancy.query.count() == 0:
            job1 = Vacancy(
                title="Software Developer",
                department="Innovation, Research & Development",
                contract_type="Contract",
                posted_date=date(2024, 11, 27),
                expiry_date=date(2024, 12, 20),
                description="Responsible for building software by writing code, modifying software, improving performance, or upgrading interfaces."
            )
            job2 = Vacancy(
                title="Regional Sales Manager",
                department="Sales",
                contract_type="Contract",
                posted_date=date(2024, 12, 4),
                expiry_date=date(2024, 12, 18),
                description="Dynamic and goal-driven Regional Sales Manager to boost revenue and lead trade operations."
            )
            db.session.add_all([job1, job2])
            db.session.commit()

    return app
