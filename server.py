

from flask import Flask, request, render_template, flash, redirect, session, jsonify
import crud
from jinja2 import StrictUndefined
from model import connect_to_db
import sys
import logging


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def root():
    """Show react template."""
    return render_template('react.html')

@app.route('/login', methods=["POST"])
def login():
    """Allow user to login """
    login_info = request.get_json() #list with username and password
    username = login_info['username']
    password = login_info['password']
    users_login = crud.get_user_by_username(username)
    
    if users_login == None:
        #flash(f'Looks like you have not made an account yet!')
        return jsonify('does not exist')
    elif users_login.password == password:
        #session['current_user'] = users_login.user_id
        #flash(f'Nice to see you back, {users_login.username}!')
        return jsonify(users_login.user_id)
    else:
        #flash(f'The password you inputed for {users_login.username} is incorrect. Try again!')
        return jsonify('incorrect password')

# @app.route('/open_create_user')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host='0.0.0.0')