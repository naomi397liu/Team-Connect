from flask import Flask, request, render_template, flash, redirect, session
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

@app.route('/search')
def search():
    """ see teammates that share your city and sport """
    #collect current user info
    flash(f"These are all the potential teammates based on your location and activity interest!")
    user_in_session = session['current_user']
    profile = crud.get_player_by_username(user_in_session)
    sport = profile.sport.sport_name
    location = profile.city.city_name
    #collect matching info
    potentials = []
    sport_potentials = crud.get_players_by_sport(sport)
    city_potentials = crud.get_players_by_city(location)
    players = crud.get_players()
    #check all players for matches
    for player in players:
        if (player in city_potentials) and (player in sport_potentials):
            potentials.append(player)
    return render_template('findteammates.html', potentials=potentials)

@app.route('/nav')
def navigate():
    """ Show Navigation page """
    return render_template("nav.html")

@app.route('/login')
def login():
    """allow user to login """
    username = request.args.get('username')
    password = request.args.get('password')

    users_login = crud.get_player_by_username(username)
    
    if users_login.password == password:
        session['current_user'] = username
        user_in_session = session['current_user']
        flash(f'Nice to see you back, {user_in_session}!')
        return redirect('/nav')
    else:
        flash(f'The password you inputed for {users_login.username} is incorrect. Try again!')
        return redirect('/')

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
        return redirect('/createuser')
    else:
        crud.create_player(username, password, bio, s, c)
        flash(f'Player created! Please login')
        return redirect('/')

@app.route('/users')
def display_user():
    """ display all users that have been created """
    users = crud.get_players()

    return render_template('users.html', users=users)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')