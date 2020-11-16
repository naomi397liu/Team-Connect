

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

fake = Faker()
#use faker
#creates a sports table
sports = ['Soccer','Basketball','Volleyball']
for sport in sports:
    crud.create_sport(sport)

#creates a cities table
cities = ['San Francisco', 'Sacramento', 'Los Angeles']
for city in cities:
    crud.create_city(city)

#creates 22 fake users with randomly chosen cities and sports from the above created tables
num=0

for num in range(22):
    username=fake.first_name()
    while crud.get_player_by_username(username) != None:
        username = fake.first_name()
    password=fake.ssn()
    bio=fake.paragraph(nb_sentences=1)
    sport = crud.get_sport_by_id(randint(1,len(sports)))
    city = crud.get_city_by_id(randint(1,len(sports)))
    crud.create_player(username, password, bio, sport, city)

#creates myuser:

# POPULATE CITIES TABLE AND SPORT TABLE


parks = ['Doloris', 'Lincoln', 'Hermosa']


