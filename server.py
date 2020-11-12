from flask import Flask, request, render_template, flash
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

# @app.route('/users', methods=["POST"])
# def users():
#     """Show profile.html template """
#     users = crud.get_players()
#     return render_template('profile.html', users=users)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')