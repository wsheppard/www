
from flask import render_template, flash, Blueprint
from flask_login import LoginManager
from flask_login import login_user , logout_user , current_user , login_required
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms_alchemy import model_form_factory
from wtforms_alchemy import ModelForm, ModelFormField, ModelFieldList, QuerySelectField
from wtforms.fields import FormField, PasswordField
from wtforms import SubmitField, validators 
from flask_wtf import FlaskForm
from flask import Flask,request,send_from_directory,render_template,redirect,url_for
from flask_sqlalchemy_session import current_session as ses

bp = Blueprint('root','root')

@bp.route("/",methods=['GET', 'POST'])
def root():
    return render_template('index.html')

@bp.route("/cv")
def cv():
    return render_template('cv.html')

@bp.route("/table")
def table():
    return render_template('table.html', nums = range(63,-1,-1)  )


@bp.route("/keypad")
def keypad():
    return render_template('keypad.html');


