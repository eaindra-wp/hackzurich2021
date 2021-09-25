from datetime import date
from markupsafe import escape
import pandas as pd
from flask import (
    Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
            SECRET_KEY='hackzurich_swica')

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        error = None
        if request.method == 'POST':
            
            username = request.form['username']
            password = request.form['password']

            if not username: 
                error = 'Username is required.'
            
            elif not password:
                error = 'Password is required.'

            if error is None:
                
                open_username_csv = pd.read_csv('username_details.csv', index_col=0)

                found_loggedin_user = open_username_csv.loc[(open_username_csv['username'] == username) & (open_username_csv['password'] == password)]
                
                if found_loggedin_user is None: 
                    error = "The user is not found. PLease check yor credentials again."

                else: 
                    session.clear()
                    session['user_id'] = found_loggedin_user['id']
                    return redirect(url_for('hello'))
                

        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('login.html', error=error)


    @app.route('/signup', methods=['POST', 'GET'])
    def signup():
        error = None
        if request.method == 'POST':

            username = request.form['username']
            password = request.form['password']
            date_of_birth = request.form['date-of-birth']

            if not username: 
                error = 'Username is required.'
            
            elif not password:
                error = 'Password is required.'
            
            elif not date_of_birth:
                error = 'Date of Birth is required.'

            if error == None:
                
                open_username_csv = pd.read_csv('username_details.csv', index_col=0)
                new_row = {'id': len(open_username_csv.index) + 1, 'username':request.form.get('username'), 'password':request.form.get('password'), 'date-of-birth': request.form.get('date-of-birth')}

                
                open_username_csv = open_username_csv.append(new_row, ignore_index=True)
                open_username_csv.to_csv("username_details.csv")
                
                
        # the code below is executed if the request method
        # was GET or the credentials were invalid
        return render_template('signup.html', error=error)



    # @app.route('/hello/')
    # @app.route('/hello/<name>')
    # def hello(name=None):
    #     return render_template('hello.html', name=name)



    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return f'User {escape(username)}'

    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return f'Post {post_id}'

    @app.route('/path/<path:subpath>')
    def show_subpath(subpath):
        # show the subpath after /path/
        return f'Subpath {escape(subpath)}'
