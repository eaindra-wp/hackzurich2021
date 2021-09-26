from flaskr import ocr
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import pandas as pd

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/', methods=('POST', 'GET'))
def index():
    return render_template("home/index.html")


@bp.route('/complete_profile', methods=('POST', 'GET'))
def complete_profile():

    result = redirect("home/")

    if request.method == 'POST':
        print('posot method')

        # get values required to save in the user profile DF from the form submitted.
        insurance_id = request.form['insurance_id']
        date_of_birth = request.form['date_of_birth']
        weight = request.form['weight']
        height = request.form['height']
        blood_group = request.form.getlist('bloodgroup')[0]
        smoking_frequency = request.form['smoking_behavior']
        drinking_frequency = request.form['drinking_behavior']

        print(insurance_id)

        user_profile_details_csv = pd.read_csv(
            'user_profile_details.csv', index_col=0)
        new_user_profile = {'id': len(user_profile_details_csv.index) + 1, 'user_id': session['user_id'], 'insurance_id': insurance_id,
                            'date_of_birth': date_of_birth, 'weight': weight, 'height': height,
                            'blood_group': blood_group, 'smoking_frequency': smoking_frequency,
                            'drinking_frequency': drinking_frequency}
        user_profile_details_csv = user_profile_details_csv.append(
            new_user_profile, ignore_index=True)
        user_profile_details_csv.to_csv("user_profile_details.csv")

        result = redirect(url_for("home.index"))

    else:
        result = render_template("home/complete_profile.html")

    return result


@bp.route('/profile', methods=('POST', 'GET'))
def profile():
    return "show profile"
