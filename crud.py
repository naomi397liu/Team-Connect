""" functions to create tables and filter/query them """
# TODO: change function names that pertain to user, to use 'user' in the name and change function names that pertain
# to a player to use 'player' in the function names
from model import db, User, Sport, Park, City, Team, Player, connect_to_db
from datetime import datetime, time

# creating data:
#1
# CITY QUERIES
def create_city(city_name):
    """ creates a city needed to create a park for the sport to be played in; needed to create user to assess 
    what parks/other users they can play in/with"""
    c=City(city_name=city_name)
    db.session.add(c)
    db.session.commit()

    return c

def get_city():
    """ displays all cities """
    return City.query.all()

def get_city_by_id(num):
    """takes in an ID and returns the object city that corresponds to it"""
    return City.query.filter_by(city_id = num).first()

# SPORT QUERIES

def create_sport(sport_name):
    """ creates a sport that is supported by a specific park; needs a park to have a sport otherwise where would you play
    needed to create player"""

    sport = Sport(sport_name=sport_name)
    db.session.add(sport)
    db.session.commit()

    return sport

def get_sport_by_id(num):
    """Takes in an ID and returns the object sport that corresponds to it"""
    return Sport.query.filter_by(sport_id = num).first()

#USER QUERIES
def create_player(user, pw, bio, sport, city):
    """ creates a new player's profile """
    user = User(username=user, password=pw, bio=bio, sport=sport, city=city)
    db.session.add(user)
    db.session.commit()
    return user

def get_players():
    """return all users"""

    return User.query.all()

def get_player_by_username(username):
    """gets a player by unique username """
    return User.query.filter(username == User.username).first()

def get_players_by_sport(sport_obj):
    """takes in a string: sport_name and outputs a list of players with that sports_name"""
     #TODO: user SQL filter_by to do this 
    teammates = []
    players = User.query.all()
    for player in players:
        if player.sport == sport_obj:
            teammates.append(player)

    return teammates

def get_players_by_city(city_obj):
    """ takes in a city_name from db and outputs a list of players with that city_name"""
    #TODO: user SQL filter_by to do this 
    teammates = []
    players = User.query.all()
    for player in players:
        if player.city == city_obj:
           teammates.append(player)
    
    return teammates

def get_player_by_id(num):
    """takes in an ID and returns object users that corresponds with it"""
    return User.query.filter_by(user_id = num).first()

#TEAM QUERIES
def create_team(name, description, user, sport, city):
    """ creates a team and takes in a team name, desciption, sport from table, city from table and park from table"""
    team = Team(team_name=name, description=description, captain=user, sport=sport, city=city)
    db.session.add(team)
    db.session.commit()

    return team

def get_teams():
    """ displays all teams """
    return Team.query.all()

def get_team_by_id(id):
    """gets the team that corresponds with the id taken in"""
    return Team.query.filter_by(team_id = id).first()

def get_team_by_teamname(name):
    """ takes in a team name and out puts the team object that corresponds with it"""
    return Team.query.filter_by(team_name = name).first()

#TEAM PLAYER QUERIES
def remove_player(player):
    """Takes in the object user and removes them as a player from a given team"""
    db.session.delete(player)
    db.session.commit()
    
    return
    
def create_team_player(phone, user, team):
    """creates a player by taking in a user object and team object to make a user a member of a team
    if the user is not already part of the team"""
    # if the user is already a player on that TEAM
    if Player.query.filter_by(user = user, team=team).first():
        player = Player.query.filter_by(user = user, team = team).first()
    else:
        player = Player(phone=phone, user=user, team=team)
        db.session.add(player)
        db.session.commit()

    return player

# def find_team_captain(user, team):
#     """Takes in the object user and object team to find the object player who is the team captain"""
def is_captain(user):
    """Find out if the user is a team captain."""
    if is_player(user):
        users_teams = get_players_teams(user)
        for team in users_teams:
            if user == team.captain:
                return True
            else:
                return False

    else: 
        return is_player(user)

def which_captain(user):
    """if you know a user is a captain, get object player. Right now a user can only create one team
    so this will always return a single object"""
    users_teams = get_players_teams(user)
    for team in users_teams:
        if user == team.captain:
            return get_player_by_user_team(user, team)

def get_player_by_user_team(user, team):
    """ Takes in an object team and object user and outputs the unique player object"""
    player = Player.query.filter_by(user = user, team = team).first()

    return player

def get_players_teams(user):
    """takes in an object user and outputs the team objects in a set for that user"""
    list_teams = Player.query.filter_by(user = user ).all()
    teams = set()
    for list_team in list_teams:
        teams.add(list_team.team)
    return teams

def is_player(user):
    """Takes in a user object and returns False if the user is not a player of any team"""
    return Player.query.filter_by(user=user).all() != []

def get_teams_players(team):
    """Takes in a team object and outputs all the players for that team """
    return Player.query.filter_by(team = team).all()

def is_new_player(user, team):
    """checks to see if this user is already a player of the team, returns T/F"""
    if Player.query.filter_by(user = user, team = team).first():
        return False
    else:
        return True

def create_park(park_name, city):
    """ takes in a park name & city from city table it is in and adds it to the park table """
    park = Park(park_name=park_name, city=city)
    db.session.add(park)
    db.session.commit()

    return park

if __name__ == '__main__':
    from server import app
    connect_to_db(app)