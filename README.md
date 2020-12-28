
<h1 align="center">
    <img width=50% alt="redLogo" src="https://user-images.githubusercontent.com/71605433/101545930-d946c380-395c-11eb-8705-89f501c1a69a.png">
    
</h1>

Team Connect is an application that unites users with the same athletic interest and who live in the same city, so that they can connect with one another to play casually. If a user has an athletic interest such as soccer, it allows the user to find others near by who would also like to play soccer. They can choose to be on the same team or play against each other. 

Visit the site here:
<a href="https://team-connect.herokuapp.com/" target="_blank">team-connect</a>

# Contents:
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Future Features](#future)

# <a name="tech-stack"></a>Technologies
- Python
- JavaScript
- AJAX
- SQL Alchemy
- PostgreSQL
- Jinja
- Flask
- jQuery
- HTML
- CSS
- Bootstrap

# <a name="features"></a>Features


## Start By Creating An Account
To participate, an individual must first become a user by creating a account. Their username must be unique. They can input a password, preferred sport and location. They can also include a blurb describing themselves as a player but it is limited to 50 characters. 

![View](https://media.giphy.com/media/P6YNDwhjvZo3XR1tXV/giphy.gif)


## Views
Once a user logs in, their profile pops up. They can also view all the users and all teams. They can also view potential teammates who share their sport and city. Potential teams are also teams that share the users sport and city. To see more details, a user can click on another user to view their profile. They can also click on a team to view more details about that team.

![View](https://media.giphy.com/media/7TptAgICyQMn7KsI8q/giphy.gif)


## Creating a Team
A user can create a team, making them the team captain. They must input a unique team name, a phone number, sport, city and details about the team. In the description and details portion, the captain can specify what day they would like to play or include a park they would like to play at. A phone number is needed so that users outside of the team can contact the captain to arrange games. 

![Create-Team](https://media.giphy.com/media/oDV0Z3FAIP8KJ8SZyk/giphy.gif)


Once the team has been created, any user can view its details. The captain is automatically listed in the team's details as well as on the players list. Each user on the player's list is clickable to view their information

![View-Team](https://media.giphy.com/media/uNCXY85sEBzzYZsUwo/giphy.gif)


## Joining a Team
Not everyone wants the responsibility of hosting a team, so a user can join a team as well. A user can view the captain's phone number before joining the team and make any inquiries about the team. Once the user joins the team, they can view any teammate's phone number to contact them for example about carpooling. 

### View Before Joining

![Before-Join](https://media.giphy.com/media/reGkKX3NPLNdk7wOks/giphy.gif)


### View After Joining

![After-join](https://media.giphy.com/media/9wGhax7qU0hVkAZJzh/giphy.gif)

### Leave
A user can also leave a team after joining by clicking the same button, but they will still have to input the phone number to leave. 

![Leave](https://media.giphy.com/media/tw5Yvki11i2NenAPDb/giphy.gif)


# <a name="future"></a> Future Features
- [ ] Allow a team captain to delete their team, which will automatically delete all the players from it as well
- [ ] If a captain removes themselves from the team, the team will be deleted
- [ ] Allow for wider range of city and sport choices
- [ ] Provide park choice or import database of parks
- [ ] Add a request game option that allows the captain to choose an opponent team, park and time/date to play at
- [ ] Add an in chat app instead of phone numbers
- [ ] Add nofication API to send notification when a game is coming up or when their is a message in their inbox


