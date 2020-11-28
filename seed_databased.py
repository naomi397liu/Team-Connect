

import os
import json
from random import choice, randint
from datetime import datetime
from faker import Faker

import crud
import model
import server

os.system('dropdb games')
os.system('createdb games')

model.connect_to_db(server.app)
model.db.create_all()

def load_required_data():
    """loads in the list of sports and cities that are supported"""
    #creates a sports table
    sports = ['Soccer','Basketball','Volleyball']
    for sport in sports:
        crud.create_sport(sport)

    #creates a cities table
    cities = ['San Francisco', 'Sacramento', 'Los Angeles']
    for city in cities:
        crud.create_city(city)
    return [sports, cities]

#creates 22 fake users with randomly chosen cities and sports from the above created tables
def load_fake_users():
    sports = load_required_data()[0]
    num=0
    fake = Faker()
    for num in range(22):
        username=fake.first_name()
        while crud.get_user_by_username(username) != None:
            username = fake.first_name()
        password=fake.ssn()
        bio=fake.paragraph(nb_sentences=1)
        sport = crud.get_sport_by_id(randint(1,len(sports)))
        city = crud.get_city_by_id(randint(1,len(sports)))
        crud.create_user(username, password, bio, sport, city)
    return

def load_fake_players():
    load_fake_users()
    fake = Faker()
    a = fake.phone_number()
    b = fake.phone_number()
    c = fake.phone_number()
    d = fake.phone_number()
    e = fake.phone_number()
    f = fake.phone_number()

    crud.create_team('Killers', 'Play to win',crud.get_user_by_id(3), crud.get_sport_by_id(1), crud.get_city_by_id(1))
    crud.create_team_player(a, crud.get_user_by_id(1), crud.get_team_by_id(1))
    crud.create_team_player(b, crud.get_user_by_id(3), crud.get_team_by_id(1))
    crud.create_team_player(c, crud.get_user_by_id(2), crud.get_team_by_id(1))
    #won't create a duplicate team player
    crud.create_team_player(d, crud.get_user_by_id(1), crud.get_team_by_id(1))

    crud.create_team('Wombats', 'Best D, greatest offense', crud.get_user_by_id(4),crud.get_sport_by_id(2), crud.get_city_by_id(2))
    crud.create_team_player(a, crud.get_user_by_id(1), crud.get_team_by_id(2))
    crud.create_team_player(e, crud.get_user_by_id(4), crud.get_team_by_id(2))


    crud.create_team('Aggies', 'Farm for Fun', crud.get_user_by_id(5),crud.get_sport_by_id(3), crud.get_city_by_id(3))
    crud.create_team_player(f, crud.get_user_by_id(5), crud.get_team_by_id(3))
    return

# auto loads everything you would need to have a fake players including required data and users
load_fake_players()