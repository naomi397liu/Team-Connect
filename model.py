""" model for PickUpBall app """
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time


db = SQLAlchemy()

class User(db.Model):
    """ A user """
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    bio = db.Column(db.String)
    
    sport_id = db.Column(db.Integer, db.ForeignKey('sports.sport_id')) #sports=tablename
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id')) #sports_id=thing we want from table
   
    sport = db.relationship('Sport', backref='users') #Sport=class referenced
    city = db.relationship('City', backref='users') #current table name -> one-to-many style
    
    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'


class Sport(db.Model):
    """ sports user can choose from """
    __tablename__ = 'sports'
    sport_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sport_name = db.Column(db.String)

    def __repr__(self):
        return f'<Sport sport_id={self.sport_id} sport_name={self.sport_name}>'

class Park(db.Model):
    """ parks certain sports can be played on """
    __tablename__ = 'parks'
    park_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    park_name = db.Column(db.String)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'))

    city = db.relationship('City', backref='parks')

    def __repr__(self):
        return f'<Park park_id={self.park_id} park_name={self.park_name}>'

class City(db.Model):
    """ cities in CA where users and/or parks may be located """
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_name = db.Column(db.String)

    def __repr__(self):
        return f'<City city_id={self.city_id} city_name={self.city_name}>'

class Team(db.Model):
    """ contains information for a given team """
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    team_name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    sport_id = db.Column(db.Integer, db.ForeignKey('sports.sport_id')) #sports=tablename
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id')) #sports_id=thing we want from table
    # park_id = db.Column(db.Integer, db.ForeignKey('parks.park_id'))

    captain = db.relationship('User', backref='teams')
    sport = db.relationship('Sport', backref='teams') #Sport=class referenced
    city = db.relationship('City', backref='teams')
    # park = db.relationship('Park', backref='teams')

    def __repr__(self):
        return f'<Team team_id={self.team_id} team_name={self.team_name}>'

# Player is defined as a user on a team. If the same user wants to be on 3 teams for example, then they would
# be 3 players, one for each team but they would all share the same object user
class Player(db.Model):
    """Contains all the players for a given team, many to many relationship/join table"""
    __tablename__ = 'players'
    player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    phone = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'))

    user = db.relationship('User', backref='players')
    team = db.relationship('Team', backref='players')

    def __repr__(self):
        return f'<Player player_id={self.player_id} user={self.user.username} team={self.team.team_name}>'
#database name = games, called with psql
def connect_to_db(flask_app, db_uri='postgres://yucpqokrcaiepe:5446752aedfb8829222b3f136c08dda397e9146093fea58c28d5f673058c8fa4@ec2-54-156-85-145.compute-1.amazonaws.com:5432/dd17anf51gtb4f'):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    db.app = flask_app #connects db to server
    db.init_app(flask_app) #initalize with flask app

    print('Connected to the db! :)')


# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)
    
#     db.create_all()


