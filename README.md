# Team Connect

### Technologies required:

- AJAX
- SQL Alchemy
- Jinja
- Flask
- Bootstrap

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


