""" functions to create tables and filter/query them """

from model import db, User, Sport, Park, City, Team, Game, Team_type, connect_to_db
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
def current_user():
    return db.session
    
def get_city():
    """ displays all cities """
    return City.query.all()

def create_park(name, city):
    """ creates a park for the sport to be played in. Needs a pre-created city for the park to exist in"""

    park = Park(park_name=name, city=city)
    db.session.add(park)
    db.session.commit()

    return park

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

# def create_availability(date_str, upper_strhr, upper_strmin, lower_strhr, lower_strmin):
#     """date the user is available to play; needed to create a player"""
#     #convert to int
#     upper_inthr=int(upper_strhr)
#     upper_intmin=int(upper_strmin)
#     lower_inthr=int(lower_strhr)
#     lower_intmin=int(lower_strmin)

#     upper = time(upper_inthr, upper_intmin) #time(1,2,3) -convert to integer: int()
#     lower = time(lower_inthr, lower_intmin)
#     format = '%a' #abbreviated day of the week
#     date = datetime.strptime(date_str, format)
#     availability = Availability(date=date, upper_time=upper, lower_time=lower) #add formating
#     db.session.add(availability)
#     db.session.commit()

#     return availability
    #  str = '11-20-2020 11:30AM'
    # format = '%m-%d-%Y %I:%M%p'
    # new_date = datetime.strptime(date_str, format)
    # check date: new_date.strftime(format)



def create_team_type(ttype):
    """ creates team type ie womens,mens,co-ed; needed to create a team"""
    team_type = Team_type(team_type=ttype)
    db.session.add(team_type)
    db.session.commit()

    return team_type

def create_game(str_start, str_end, location):
    """ takes in a start date&time, end date&time, and park as location. It outputs a game. relies on pre-created park"""
    # str = '11-20-2020 11:30AM'
    # format = '%m-%d-%Y %I:%M%p'
    # new_date = datetime.strptime(date_str, format)
    # check date: new_date.strftime(format)
    format = '%m-%d-%Y %I:%M%p'
    start = datetime.strptime(str_start, format)
    end = datetime.strptime(str_end, format)
    game = Game(start_time=start, end_time=end, park=location) #format date
    db.session.add(game)
    db.session.commit()

    return game

def create_team(name, game, team_type):
    """ creates a team, but requires a precreated game time and team_type """
    team = Team(team_name=name, game=game, team_type=team_type)
    db.session.add(team)
    db.session.commit()

    return team


if __name__ == '__main__':
    from server import app
    connect_to_db(app)