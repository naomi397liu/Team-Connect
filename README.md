
<h1 align="center">
    <img width=50% alt="redLogo" src="https://user-images.githubusercontent.com/71605433/101545930-d946c380-395c-11eb-8705-89f501c1a69a.png">
    
</h1>

Team Connect is an application that unites users with the same athletic interest and who live in the same city, so that they can connect with one another to play casually. If a user has an athletic interest such as soccer, it allows the user to find others near by who would also like to play soccer. They can choose to be on the same team or play against each other. 

## Contents:
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Future Features](#future)

## <a name="tech-stack"></a>Technologies
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

## <a name="features"></a>Features

### Start By Creating An Account
To participate, an individual must first become a user by creating a account. Their username must be unique. They can input a password, preferred sport and location. They can also include a blurb describing themselves as a player but it is limited to 50 characters. 

<iframe src="https://giphy.com/embed/P6YNDwhjvZo3XR1tXV" allowFullScreen></iframe>
<!-- <p><a href="https://giphy.com/gifs/P6YNDwhjvZo3XR1tXV">via GIPHY</a></p> -->


### Data

**Built in sports and cities**

- A user contains data on what their sport of interest is and their city
- A team contains data on their sport, city and team captain AKA the creator of the team 
- A player creates a many to many relationship through a linked table between teams and users

### Roadmap 

- [x] Allow users to create profiles in order to be linked up with others that share their location and sports interest(MVP)
- [x] Allow users to create teams that are added to the database
- [x] Allow users to join teams
- [x] Allow users to leave teams
- [x] Allow teammates to see each other's phone numbers to contact one another
- [x] Allow any user to view a team captain's phone number to arrange games against that team
- [x] Allow users to view potential teammates
- [x] Allow users to view potential teams they could join

**Version 2.0: Future Features**
- [ ] Separate testdb
- [ ] JS testing
- [ ] Allow a team captain to delete their team, which will automatically delete all the players from it as well
- [ ] If a captain removes themselves from the team, the team will be deleted
- [ ] Importing parks API that support a given sport and provide the city it correlates to
- [ ] Add a request game option that allows the captain to choose an opponent team, park and time/date to play at
- [ ] Add an in chat app instead of phone numbers
- [ ] Add twilio api to send notification when a game is coming up or when their is a message in their inbox


