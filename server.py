from flask import Flask, request, render_template, flash, redirect
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def login():
    """Show hello.html template."""
    return render_template('homepage.html')

@app.route('/createuser')
def create_user():
    """Show greet.html template """
    # user = create_player(user, pw, bio, sport, city)
    return render_template('createuser.html')

@app.route('/nav')
def navigate():
    """ Show Navigation page """
    return render_template("nav.html")

@app.route('/users', methods=["POST"])
def register_user():
    """Show profile.html template """
    #create city
    city = request.form.get('cities')
    crud.create_city(city)
    flash('City created! Please log in.')
    #create sport

    #create player
    # user_id = session['user_id']

    # users = crud.get_players()
    return redirect('/nav')

@app.route('/users')
def display_user():
    """ display all users that have been created """
    cities = crud.get_city()

    return render_template('users.html', cities=cities)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')