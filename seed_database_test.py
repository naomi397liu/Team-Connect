#variable names give for experimentation with different methodologies/fucntions
#  to be implemented in server.py
# for possible database feature additions


import os
import json
from random import choice, randint
from faker import Faker

import crud
from model import db, connect_to_db
import server

os.system('dropdb test')
os.system('createdb test')

connect_to_db(server.app)
db.drop_all()
db.create_all()

def load_test():
    os.system('dropdb test')
    os.system('createdb test')

    connect_to_db(server.app)   
    db.drop_all()
    db.create_all()
    """ loads in all the test data"""
    sports = ['Soccer','Basketball','Volleyball']
    for sport in sports:
        crud.create_sport(sport)

    #creates a cities table
    cities = ['San Francisco', 'Sacramento', 'Los Angeles']
    for city in cities:
        crud.create_city(city)


    #creates 22 fake users with randomly chosen cities and sports from the above created tables


    num=0
    fake = Faker()
    username = 'test_user1'
    password = 'test_pass1'
    sport = 'Soccer'
    city = 'San Francisco'
    bio = 'Test user created for testing'
    crud.create_user(username, password, bio, crud.get_sport_by_id(2), crud.get_city_by_id(3))
    # model.User(username=username, password=password, bio=bio, sport=sport, city=city)
    for num in range(22):
        username=fake.first_name()
        while crud.get_user_by_username(username) != None:
            username = fake.first_name()
        password=fake.ssn()
        bio=fake.paragraph(nb_sentences=1)
        sport = crud.get_sport_by_id(randint(1,len(sports)))
        city = crud.get_city_by_id(randint(1,len(sports)))
        crud.create_user(username, password, bio, sport, city)




    fake = Faker()
    a = fake.phone_number()
    b = fake.phone_number()
    c = fake.phone_number()
    d = fake.phone_number()
    e = fake.phone_number()
    f = fake.phone_number()

    team1 = crud.create_team('Killers', 'Play to win',crud.get_user_by_id(3), crud.get_sport_by_id(1), crud.get_city_by_id(1))
    # player1 = crud.create_team_player(a, crud.get_user_by_id(1), crud.get_team_by_id(1))
    player2 = crud.create_team_player(b, crud.get_user_by_id(3), crud.get_team_by_id(1))
    # player3 = crud.create_team_player(c, crud.get_user_by_id(2), crud.get_team_by_id(1))
    #won't create a duplicate team player
    # player4 = crud.create_team_player(d, crud.get_user_by_id(1), crud.get_team_by_id(1))

    team2 = crud.create_team('Wombats', 'Best D, greatest offense', crud.get_user_by_id(4),crud.get_sport_by_id(2), crud.get_city_by_id(2))
    player5 = crud.create_team_player(a, crud.get_user_by_id(1), crud.get_team_by_id(2))
    player6 = crud.create_team_player(e, crud.get_user_by_id(4), crud.get_team_by_id(2))


    team3 = crud.create_team('Aggies', 'Farm for Fun', crud.get_user_by_id(5),crud.get_sport_by_id(3), crud.get_city_by_id(3))
    player7 = crud.create_team_player(f, crud.get_user_by_id(5), crud.get_team_by_id(3))
    return
#creates myuser:
load_test()