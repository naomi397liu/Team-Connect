from flask import Flask, request, render_template, flash, redirect
import crud
from jinja2 import StrictUndefined
from model import connect_to_db

app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_login():
    """Show hello.html template."""
    return render_template('homepage.html')

@app.route('/createuser')
def create_user():
    """Show greet.html template """
    # user = create_player(user, pw, bio, sport, city)
    return render_template('createuser.html')

@app.route('/nav')
def navigate():
    """ Show Navigation page """
    return render_template("nav.html")

@app.route('/nav,', methods=["POST"])
def login():
    """allow user to login """

@app.route('/users', methods=["POST"])
def register_user():
    """create user template """
    #create city
    city = request.form.get('cities')
    c = crud.create_city(city) 
    #create sport
    sport = request.form.get('sports')
    s = crud.create_sport(sport)
    
    #create player
    username = request.form.get('username')
    password = request.form.get('password')
    bio = request.form.get('bio')
    if crud.get_player_by_username(username):
        flash(f'Sorry! That username is already in use!')
    else:
        user = crud.create_player(username, password, bio, s, c)
        flash(f'Hi, {user.username}! You are now logged in.')
        return redirect('/nav')

@app.route('/users')
def display_user():
    """ display all users that have been created """
    users = crud.get_players()

    return render_template('users.html', users=users)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')