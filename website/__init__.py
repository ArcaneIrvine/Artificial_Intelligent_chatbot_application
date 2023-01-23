import os
from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# define new database
db = SQLAlchemy()
DB_NAME = "database.db"


# app create function
def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(12).hex()
    # store database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # initialize database
    db.init_app(app)

    # register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # create database
    from .models import User, Note
    create_database(app)

    return app


# database create function
def create_database(app):
    if not path.exists('website/'+DB_NAME):
        with app.app_context():
            db.create_all()
            print('database created')

