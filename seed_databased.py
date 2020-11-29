

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


#creates a sports table
sports = ['Soccer','Basketball','Volleyball']
for sport in sports:
    crud.create_sport(sport)

#creates a cities table
cities = ['San Francisco', 'Sacramento', 'Los Angeles']
for city in cities:
    crud.create_city(city)

