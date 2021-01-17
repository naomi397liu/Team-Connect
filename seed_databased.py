

import os
import json
from random import choice, randint
from faker import Faker

import crud
from model import db, connect_to_db
import server

# os.system('dropdb games')
# os.system('createdb games')

connect_to_db(server.app)
# db.drop_all()
db.create_all()


def load_required():
    
    """ loads in all the test data"""
    sports = ['Soccer','Basketball','Volleyball']
    for sport in sports:
        crud.create_sport(sport)

    #creates a cities table
    cities = ['San Francisco', 'Sacramento', 'Los Angeles']
    for city in cities:
        crud.create_city(city)
    return [sports, cities]

    #creates 22 fake users with randomly chosen cities and sports from the above created tables

def load_test():
    sports = load_required()[0]
    num=0
    fake = Faker()
    username = 'test_user1'
    password = 'test_pass1'
    sport = 'Soccer'
    city = 'San Francisco'
    bio = 'Test user created for testing'
    crud.create_user(username, password, bio, crud.get_sport_by_id(2), crud.get_city_by_id(3))
    # model.User(username=username, password=password, bio=bio, sport=sport, city=city)
    for num in range(40):
        username=fake.first_name()
        while crud.get_user_by_username(username) != None:
            username = fake.first_name()
        password=fake.ssn()
        bio=fake.paragraph(nb_sentences=1)
        sport = crud.get_sport_by_id(randint(1,len(sports)))
        city = crud.get_city_by_id(randint(1,len(sports)))
        crud.create_user(username, password, bio, sport, city)
    


    crud.create_team('Killers', 'Play to win', crud.get_user_by_id(1), crud.get_sport_by_id(1), crud.get_city_by_id(1))
    for num in range(1, 4):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(1))
    
            
    crud.create_team('Wombats', 'Best D, greatest offense', crud.get_user_by_id(4),crud.get_sport_by_id(2), crud.get_city_by_id(2))
    for num in range(4, 10):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(2))

    crud.create_team('Cougars', 'Come play on Saturdays!', crud.get_user_by_id(10),crud.get_sport_by_id(1), crud.get_city_by_id(2))
    for num in range(10,19):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(3))

    crud.create_team('Wolves', 'Play ball with me on Tuesday nights!', crud.get_user_by_id(19),crud.get_sport_by_id(2), crud.get_city_by_id(1))
    for num in range(19, 25):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(4))

    crud.create_team('Sharks', 'Speedsters! Playing every weekend!', crud.get_user_by_id(25),crud.get_sport_by_id(3), crud.get_city_by_id(3))
    for num in range(25, 29):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(5))

    crud.create_team('Banana Slugs', 'Play to win',crud.get_user_by_id(29), crud.get_sport_by_id(1), crud.get_city_by_id(1))
    for num in range(29, 36):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(6))

    crud.create_team('Peach Eaters', 'Best D, greatest offense', crud.get_user_by_id(35),crud.get_sport_by_id(2), crud.get_city_by_id(2))
    for num in range(35, 36):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(7))

    crud.create_team('Cat Lovers', 'Farm for Fun', crud.get_user_by_id(36),crud.get_sport_by_id(3), crud.get_city_by_id(3))
    for num in range(36, 37):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(8))

    crud.create_team('Shark Eaters', 'Come play on Saturdays!', crud.get_user_by_id(37), crud.get_sport_by_id(1), crud.get_city_by_id(2))
    for num in range(37, 38):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(9))

    crud.create_team('Speedsters', 'Play ball with me on Tuesday nights!', crud.get_user_by_id(38),crud.get_sport_by_id(2), crud.get_city_by_id(1))
    for num in range(38, 39):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(10))

    crud.create_team('Croissant Eaters', 'Speedsters! Playing every weekend!', crud.get_user_by_id(39),crud.get_sport_by_id(3), crud.get_city_by_id(3))
    for num in range(39, 41):
        phone = fake.phone_number()
        new_player = crud.create_team_player(phone, crud.get_user_by_id(num), crud.get_team_by_id(11))

    return

#can either load in test seed data in the games database or call the function to just load
#in the minimum required data into the games database
load_test()

