from flaskr import ocr
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from numpy import string_
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import pandas as pd

bp = Blueprint('auth', __name__, url_prefix='/auth')



@bp.route('/signup', methods=('POST', 'GET'))
def signup():
    
    return_result = render_template("auth/signup.html")

    error_firstname = None
    error_lastname = None
    error_password = None
    error_repassword = None
    error_email = None
    error_phonenumber = None
    error_passwords_unmatched = None

    if request.method == 'POST':

        firstname = request.form['first_name']
        lastname = request.form['last_name']
        password = request.form['password']
        re_password = request.form['re_password']
        email = request.form['email']
        phone_number = request.form['phone_number']

        
        if not firstname:
            error_firstname = "First name is required."
            
        if not lastname:
            error_lastname = "Last name is required."
            

        if not password:
            error_password = "Password is required."
            

        if not re_password:
            error_repassword = "You need to retype the password."
            

        if password and re_password and password != re_password:
            print(password, re_password)
            error_passwords_unmatched = "The passwords in both fields should be the same."
            

        if not phone_number:
            error_phonenumber = "Phone number is required."

        if not email:
             error_email = "Email is required."
        

        if error_firstname or error_lastname or error_email or error_password or error_passwords_unmatched or error_repassword or error_phonenumber:

            return_result = render_template("auth/signup.html", error_firstname=error_firstname, error_lastname=error_lastname,
            error_email=error_email, error_password=error_password, error_passwords_unmatched=error_passwords_unmatched, 
            error_phonenumber=error_phonenumber, error_repassword = error_repassword,
            filled_firstname=firstname, filled_lastname=lastname, 
            filled_email=email, filled_phonenumber = phone_number)
        

        else: 
            open_username_csv = pd.read_csv(
                'user_signup_details.csv', index_col=0)
            new_row = {'id': len(open_username_csv.index) + 1, 'email': email, 'first_name' : firstname,
                       'last_name' : lastname, 'phone_number' : phone_number,
                       'password': password}

            open_username_csv = open_username_csv.append(
                new_row, ignore_index=True)
            open_username_csv.to_csv("user_signup_details.csv")

            return_result = redirect("login")

    return return_result




@bp.route('/login', methods=('POST', 'GET'))
def login():

    return_result = render_template("auth/login.html")

    error_password = None
    error_email = None
    error_wrong_credentials =  None

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        if not email:
            error_email = 'Username is required.'

        if not password:
            error_password = 'Password is required.'
        
        else:
            user_signup_details = pd.read_csv(
                'user_signup_details.csv', index_col=0)

            logged_in_userid = user_signup_details.loc[(
                user_signup_details['email'] == email) & (user_signup_details['password'] == password), 'id'].values[0]

            if logged_in_userid is None:
                error_wrong_credentials = "User is not found. Please check yor credentials again."
                return_result = render_template('auth/login.html', error_email=error_email, error_password=error_password, 
                    error_wrong_credentials=error_wrong_credentials)

            else:
                session.clear()
                session['user_id'] = str(logged_in_userid)

                user_profile_details = pd.read_csv('user_profile_details.csv', index_col=0)
                loggedin_user_profile_id =  user_profile_details.loc[(
                user_profile_details['user_id'] == logged_in_userid), 'id'].values[0]

                if loggedin_user_profile_id is None:
                    return_result = redirect(url_for("home.complete_profile"))

                else: 
                    return_result = redirect(url_for("home.home"))


    return return_result



def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        open_username_csv = pd.read_csv(
                'user_signup_details.csv', index_col=0)
        g.user = open_username_csv.loc[(
                open_username_csv['id'] == int(user_id))].values[0]


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
