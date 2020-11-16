""" functions to create tables and filter/query them """

from model import db, User, Sport, Park, City, Team, connect_to_db
from datetime import datetime, time

# creating data:
#1
def create_city(city_name):
    """ creates a city needed to create a park for the sport to be played in; needed to create user to assess 
    what parks/other users they can play in/with"""
    c=City(city_name=city_name)
    db.session.add(c)
    db.session.commit()

    return c

def get_players_by_sport(sport_name):
    """takes in a string: sport_name and outputs a list of players with that sports_name"""
     #TODO: user SQL filter_by to do this 
    teammates = []
    players = User.query.all()
    for player in players:
        if (player.sport.sport_name).lower() == (sport_name).lower():
            teammates.append(player)

    return teammates

def get_players_by_city(city_name):
    """ takes in a city_name from db and outputs a list of players with that city_name"""
    #TODO: user SQL filter_by to do this 
    teammates = []
    players = User.query.all()
    for player in players:
        if (player.city.city_name) == city_name:
           teammates.append(player)
    
    return teammates


def get_city():
    """ displays all cities """
    return City.query.all()

def get_sport_by_id(num):
    """Takes in an ID and returns the object sport that corresponds to it"""
    return Sport.query.filter_by(sport_id = num).first()

def get_city_by_id(num):
    """takes in an ID and returns the object city that corresponds to it"""
    return City.query.filter_by(city_id = num).first()
#2
def create_sport(sport_name):
    """ creates a sport that is supported by a specific park; needs a park to have a sport otherwise where would you play
    needed to create player"""

    sport = Sport(sport_name=sport_name)
    db.session.add(sport)
    db.session.commit()

    return sport
#3
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

def create_team(name, description, sport, city):
    """ creates a team and takes in a team name, desciption, sport from table, city from table and park from table"""
    team = Team(team_name=name, description=description, sport=sport, city=city)
    db.session.add(team)
    db.session.commit()

    return team

def create_park(park_name, city):
    """ takes in a park name & city from city table it is in and adds it to the park table """
    park = Park(park_name=park_name, city=city)
    db.session.add(park)
    db.session.commit()

    return park

if __name__ == '__main__':
    from server import app
    connect_to_db(app)