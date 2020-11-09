""" functions to create tables and filter/query them """

from model import db, User, Sport, Park, City, Team, Game, Availability, Team_type, connect_to_db
from datetime import datetime

# creating data:
def create_city(name):
    """ creates a city needed to create a park for the sport to be played in; needed to create user to assess 
    what parks/other users they can play in/with"""
    city = City(city_name=name)
    db.session.add(city)
    db.session.commit()

    return city

def create_park(name, city):
    """ creates a park for the sport to be played in. Needs a pre-created city for the park to exist in"""

    park = Park(park_name=name, city=city)
    db.session.add(park)
    db.session.commit()

    return park

def create_sport(sport_name, park):
    """ creates a sport that is supported by a specific park; needs a park to have a sport otherwise where would you play
    needed to create player"""

    sport = Sport(sport_name, park)
    db.session.add(sport)
    db.session.commit()

    return sport

def create_availability(date):
    """date the user is available to play; needed to create a player"""
    availability = Availability(date)
    db.session.add(availability)
    db.session.commit()

    return availability

def create_player(user, pw, bio, sport, city, team, avail):
    """ creates a new player's profile """
   
    user = User(user, pw, bio, sport, city, team, avail)
    db.session.add(user)
    db.session.commit()
    return user

def create_team_type(ttype):
    """ creates team type ie womens,mens,co-ed; needed to create a team"""
    team_type = Team_type(ttype)
    db.session.add(team_type)
    db.session.commit()

    return team_type

def create_game(start, end, location):
    """ takes in a start date&time, end date&time, and park as location. It outputs a game. relies on pre-created park"""

    game = Game(start, end, location)
    db.session.add(game)
    db.session.commit()

    return game

def create_team(name, game, team_type):
    """ creates a team, but requires a precreated game time and team_type """
    team = Team(name, game, team_type)
    db.session.add(team)
    db.session.commit()

    return team


if __name__ == '__main__':
    from server import app
    connect_to_db(app)