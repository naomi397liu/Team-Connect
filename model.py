""" model for PickUpBall app """
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

class User(db.model):
    """ A user """
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    bio = db.Column(db.String)
    availability_id = db.Column(db.datetime) #instead of another table
    
    sports_id = db.Column(db.Integer, dbForeignKey('sports.sports_id')) #sports=tablename
    city_id = db.Column(db.Integer, dbForeginKey('cities.city_id')) #sports_id=thing we want from table
    team_id = db.Column(db.Integer, dbForeignKey('teams.team_id'))

    #gets us other table to create a relationship between
    sport = db.relationship('Sport', backref='users') #Sport=class referenced
    city = db.relationship('City', backref='users') #current table name -> one-to-many style
    availability = db.relationship('Availability', backref='users')
    team = db.relationships('Team', backref='users')

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'

class Sport(db.model):
    """ sports user can choose from """
    __tablename__ = 'sports'
    sport_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sport_name = db.Column(db.String)
    
    capatible_parks_id = db.Column(db.Integer, dbForeignKey('parks.park_id'))

    park = db.relationship('Park', backref='sports')

    def __repr__(self):
        return f'<Sport sport_id={self.sport_id} sport_name={self.sport_name}>'

class Park(db.model):
    """ parks certain sports can be played on """
    __tablename__ = 'parks'
    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String)
    #include address if I already have the park name and city?
    city_location_id = db.Column(db.Integer, dbForeignKey('cities.city_id'))

    city = db.relationship('City', backref='parks')

    def __repr__(self):
        return f'Park park_id={self.park_id} park_name={self.park_name}>'

class City(db.model):
    """ cities in CA where users and/or parks may be located """
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_name = db.Column(db.String)
    #no foreign key because city doesn't pull from any other table, tables pull from it
    def __repr__(self):
        return f'City city_id={self.city_id} city_name={self.city_name}>'

class Team(db.model):
    """ contains information for a given team """
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_name = db.Column(db.String)
    
    players_ids = db.Column(db.Integer, dbForeginKey('users.user_id'))
    practice_id = db.Column(db.Integer, dbForeginKey('practices.practice_id'))
    game_id = db.Column(db.Integer, dbForeginKey('games.game_id'))
    team_type_id = db.Column(db.Integer, dbForeginKey('teams.team_type_id'))

    player = db.relationship('User', backref='teams')
    practice = db.relationship('Practice', backref='teams')
    game = db.relationship('Game', backref='teams')
    team_type = db.relationship('Team_type', backref='teams')

    def __repr__(self):
        return f'Team team_id={self.team_id} team_name={self.team_name}>'

class Practice(db.model):
    """ contains information about practices"""
    __tablename__ = 'practices'
    #excluded reoccurring option because idk how I would make the day and time 
    #repeat each week. Maybe extra little feature that I could add
    practice_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time = db.Column(db.datetime)
    end_time = db.Column(db.datetime)
    
    location_id = db.Column(db.Integer, dbForeignKey('parks.park_id'))

    location = db.relationship('Park', backref='practices')

    def __repr__(self):
        return f'Practice practice_id={self.practice_id} start_time={self.start_time}>'

class Game(db.model):
    """ contains information about games """
    __tablename__ = 'games'

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time = db.Column(db.datetime)
    end_time = db.Column(db.datetime)

    #opponent would be a team but a different team.... not sure how to represent
    opponent_id = db.Column(db.Integer, dbForeignKey('teams.team_id'))
    location_id = db.Column(db.Integer, dbForeignKey('parks.park_id'))

    opponent = db.relationship('Team', backref='games')
    location = db.relationship('Park', backref='games')

    def __repr__(self):
        return f'Game game_id={self.game_id} start_time={self.start_time}>'

class Team_type(db.model):
    """ indicates coed, womens or mens team """
    __tablename__ = 'team_type'

    team_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_type = db.Column(String)

    def __repr__(self):
        return f'Team_type team_type_id={self.team_type_id} team_type={self.team_type}>'










