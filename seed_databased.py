

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

a = fake.phone_number()
b = fake.phone_number()
c = fake.phone_number()
d = fake.phone_number()
e = fake.phone_number()
f = fake.phone_number()

team1 = crud.create_team('Killers', 'Play to win',crud.get_player_by_id(3), crud.get_sport_by_id(1), crud.get_city_by_id(1))
player1 = crud.create_team_player(a, crud.get_player_by_id(1), crud.get_team_by_id(1))
player2 = crud.create_team_player(b, crud.get_player_by_id(3), crud.get_team_by_id(1))
player3 = crud.create_team_player(c, crud.get_player_by_id(2), crud.get_team_by_id(1))
player4 = crud.create_team_player(d, crud.get_player_by_id(1), crud.get_team_by_id(1))

team2 = crud.create_team('Wombats', 'Best D, greatest offense', crud.get_player_by_id(4),crud.get_sport_by_id(2), crud.get_city_by_id(2))
player5 = crud.create_team_player(a, crud.get_player_by_id(1), crud.get_team_by_id(2))
player6 = crud.create_team_player(e, crud.get_player_by_id(4), crud.get_team_by_id(2))


team3 = crud.create_team('Aggies', 'Farm for Fun', crud.get_player_by_id(5),crud.get_sport_by_id(3), crud.get_city_by_id(3))
player7 = crud.create_team_player(f, crud.get_player_by_id(5), crud.get_team_by_id(3))
#creates myuser:

# POPULATE CITIES TABLE AND SPORT TABLE


parks = ['Doloris', 'Lincoln', 'Hermosa']


user1 = crud.get_player_by_id(1)
my_user = crud.get_player_by_id(3)
if (crud.is_player(user1)) and (crud.is_player(my_user)): #both false
    users_teams = crud.get_players_teams(user1) #team objects in a set
#check if the current user is a player and get current users team ids in a set
    my_users_teams = crud.get_players_teams(my_user)
#check for set overlap: if user and current user share a same team id then get users phone number
    shared_teams = users_teams & my_users_teams