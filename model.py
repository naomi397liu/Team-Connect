""" model for PickUpBall app """
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()

class User(db.Model):
    """ A user """
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    bio = db.Column(db.String)
    availability = db.Column(db.DateTime) #instead of another table
    
    sport_id = db.Column(db.Integer, db.ForeignKey('sports.sport_id')) #sports=tablename
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id')) #sports_id=thing we want from table
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'))
    #User.sports_id = sports.sports_id
    #gets us other table to create a relationship between
    #lucia: confirm one to many relationship connection backref = one, 1st arg = many
    sport = db.relationship('Sport', backref='users') #Sport=class referenced
    city = db.relationship('City', backref='users') #current table name -> one-to-many style
    team = db.relationship('Team', backref='users')

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'

class Sport(db.Model):
    """ sports user can choose from """
    __tablename__ = 'sports'
    sport_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sport_name = db.Column(db.String)
    
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'))

    park = db.relationship('Park', backref='sports')

    def __repr__(self):
        return f'<Sport sport_id={self.sport_id} sport_name={self.sport_name}>'

class Park(db.Model):
    """ parks certain sports can be played on """
    __tablename__ = 'parks'
    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String)
    #include address if I already have the park name and city?
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))

    city = db.relationship('City', backref='parks')

    def __repr__(self):
        return f'Park park_id={self.park_id} park_name={self.park_name}>'

class City(db.Model):
    """ cities in CA where users and/or parks may be located """
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_name = db.Column(db.String)
    #no foreign key because city doesn't pull from any other table, tables pull from it
    def __repr__(self):
        return f'City city_id={self.city_id} city_name={self.city_name}>'

class Team(db.Model):
    """ contains information for a given team """
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_name = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    practice_id = db.Column(db.Integer, db.ForeignKey('practices.practice_id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'))
    team_type_id = db.Column(db.Integer, db.ForeignKey('teams.team_type_id'))

    user = db.relationship('User', backref='teams')
    practice = db.relationship('Practice', backref='teams')
    game = db.relationship('Game', backref='teams')
    team_type = db.relationship('Team_type', backref='teams')

    def __repr__(self):
        return f'Team team_id={self.team_id} team_name={self.team_name}>'

class Practice(db.Model):
    """ contains information about practices"""
    __tablename__ = 'practices'
    #excluded reoccurring option because idk how I would make the day and time 
    #repeat each week. Maybe extra little feature that I could add
    practice_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'))

    park = db.relationship('Park', backref='practices')

    def __repr__(self):
        return f'Practice practice_id={self.practice_id} start_time={self.start_time}>'

class Game(db.Model):
    """ contains information about games """
    __tablename__ = 'games'

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    #lucia
    #opponent would be a team but a different team.... not sure how to represent
    opponent_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'))
    park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'))

    opponent = db.relationship('Team', backref='games')
    park = db.relationship('Park', backref='games')

    def __repr__(self):
        return f'Game game_id={self.game_id} start_time={self.start_time}>'

class Team_type(db.Model):
    """ indicates coed, womens or mens team """
    __tablename__ = 'team_type'

    team_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_type = db.Column(db.String)

    def __repr__(self):
        return f'Team_type team_type_id={self.team_type_id} team_type={self.team_type}>'


#lucia
#database name = games, called with psql
def connect_to_db(flask_app, db_uri='postgresql:///games', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app #connects db to server
    db.init_app(flask_app) #initalize with flask app

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)





