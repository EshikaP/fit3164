from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os 
from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
from base64 import b64encode
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image
from skimage.transform import resize 
import matplotlib.pyplot as plt 
from datetime import date
import tensorflow as tf 
import numpy as np 
import cv2

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    TEMPLATE_DIR = os.path.abspath('templates')
    STATIC_DIR = os.path.abspath('templates/static')
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

    app.config['SECRET_KEY'] = 'cancerimaging_aws'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
