#TODO:add asset for profile pictures

from flask import Flask, request, render_template, flash, redirect, session, jsonify
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

@app.route('/users', methods=["POST"])
def register_user():
    """create user and adds them to the database"""
    #create city
    city_id = request.form.get('cities')
    c = crud.get_city_by_id(city_id) 
    #create sport
    sport_id = request.form.get('sports')
    s = crud.get_sport_by_id(sport_id)
    
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

@app.route('/login')
def login():
    """allow user to login """
    username = request.args.get('username')
    password = request.args.get('password')

    users_login = crud.get_player_by_username(username)
    
    if users_login == None:
        flash(f'Looks like you have not made an account yet!')
        return redirect('/')
    elif users_login.password == password:
        session['current_user'] = users_login.user_id
        flash(f'Nice to see you back, {users_login.username}!')
        return redirect('/nav')
    else:
        flash(f'The password you inputed for {users_login.username} is incorrect. Try again!')
        return redirect('/')

@app.route('/nav')
def navigate():
    """ Show Navigation page """
    return render_template("nav.html")

@app.route('/users')
def display_user():
    """ display all users that have been created """
    users = crud.get_players()

    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def show_player(user_id):
    """Show details of a particular player """
    #if user is player then get their user id and put their team ids in a set
    user_profile = crud.get_player_by_id(user_id)
    my_user = crud.get_player_by_id(session['current_user'])
    if (crud.is_player(user_profile)) and (crud.is_player(my_user)):
        users_teams = crud.get_players_teams(user_profile) #team objects in a set
    #check if the current user is a player and get current users team ids in a set
        my_users_teams = crud.get_players_teams(my_user)
    #check for set overlap: if user and current user share a same team id then get users phone number
        shared_teams = users_teams & my_users_teams
    #else make phone number a str: 'Sorry but you're not teammates yet!
    #pass the str into the rendered page
    #get player obj from team
        players =[]
        for shared_team in shared_teams:
            players.append(crud.get_player_by_user_team(user_profile, shared_team))
    elif crud.is_captain(user_profile):
        player_captain = crud.which_captain(user_profile)
        players = [player_captain]
        shared_teams = [player_captain.team]
    else:
        shared_teams = None
        players = None

    
    return render_template('user_details.html', user_profile = user_profile, shared_teams=shared_teams, players=players)

@app.route('/search')
def search():
    """ see teammates that share your city and sport """
    #collect current user info
    flash(f"These are all the potential teammates based on your location and activity interest!")
    profile = crud.get_player_by_id(session['current_user'])
    #collect matching info
    potentials = []
    sport_potentials = crud.get_players_by_sport(profile.sport)
    city_potentials = crud.get_players_by_city(profile.city)
    users = crud.get_players()
    #check all players for matches
    for user in users:
        if (user in city_potentials) and (user in sport_potentials):
            potentials.append(user)
    return render_template('findteammates.html', potentials=potentials)

@app.route('/teams')
def display_teams():
    """ displays all teams"""
    teams = crud.get_teams()
    return render_template('teams.html', teams=teams)

@app.route('/createteam')
def create_team():
    """ form to create new team is rendered """
    
    return render_template("createteam.html")

@app.route('/teams', methods=["POST"])
def register_team():
    #TODO: add park portion thru ajax, such when a city is selected, only parks in that city show
    team_name = request.form.get('team_name')
    description = request.form.get('description')
    city_id = request.form.get('cities')
    phone = request.form.get('phone')
    team_city = crud.get_city_by_id(city_id) #change to crud.get_city(city)
    captain = crud.get_player_by_id(session['current_user'])
    #create the sport
    sport_id = request.form.get('sports')
    team_sport = crud.get_sport_by_id(sport_id) #get_sport_by_id
    #create park
    # park = request.form.get('park')
    # teams_park = crud.create_park(park, team_city)
    # TODO: my_session = session['my_teams'][crud.get_team_by_id(team_id).team_id] assuming one user could 
    # have already created a team
    if crud.is_captain(captain):
        team = crud.which_captain(captain).team
        players = crud.get_teams_players(team)
        flash(f'Sorry, but you already have a team that you are a captain of!')
        return render_template('team_details.html', team=team, players=players)
    elif crud.get_team_by_teamname(team_name):
        flash(f'Sorry! That team name is already in use!')
        return redirect('/createteam')
    else:
        my_team = crud.create_team(team_name, description, captain, team_sport, team_city)
        session['my_teams'] = my_team.team_id
        crud.create_team_player(phone, captain, crud.get_team_by_id(session['my_teams']))
    
        flash(f'Your team {my_team.team_name} has been created!')
        return redirect('/teams')


@app.route('/teams/<team_id>')
def show_team(team_id):
    """Show details of a particular team """

    team = crud.get_team_by_id(team_id)
    players = crud.get_teams_players(team)
    session['current_team'] = team_id #stores the team id of the current team page user in on

    return render_template('team_details.html', team=team, players=players)


@app.route('/add.json')
def add_player():
    user_id = session['current_user']
    team_id = session['current_team']
    phone = request.args.get('phone')
    user = crud.get_player_by_id(user_id)
    team = crud.get_team_by_id(team_id)
    if crud.is_new_player(user,team):
        x = 'new player!'
        new_player = crud.create_team_player(phone, user, team) 
        new_player = new_player.user.username
    else:
        x = 'already player!'
        current_player = crud.get_player_by_user_team(user,team)
        crud.remove_player(current_player)
        new_player = user.username
    # new_player = crud.create_team_player(phone, user, team) 
    # new_player = new_player.user.username
    return jsonify(new_player, user_id, x)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')