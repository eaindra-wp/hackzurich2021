from flaskr import ocr
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from numpy import string_
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import pandas as pd

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/', methods=('POST', 'GET'))
def index():
    return render_template("home/index.html")

@bp.route('/complete_profile', methods=('POST', 'GET'))
def complete_profile():
    return "complete profile here"

@bp.route('/profile', methods=('POST', 'GET'))
def profile():
    return "show profile"
