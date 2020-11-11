from flask import Flask, request, render_template
import crud

app = Flask(__name__)

@app.route('/')
def login():
    """Show hello.html template."""

    return render_template('homepage.html')

@app.route('/createuser')
def create_user():
    """Show greet.html template """

    return render_template('createuser.html')

@app.route('/nav')
def navigate():
    """ Show Navigation page """

    return render_template("nav.html")

@app.route('/users')
def users():
    """Show profile.html template """
    users = crud.get_players()
    return render_template('profile.html', users=users)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')