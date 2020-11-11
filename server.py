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

# @app.route('/display_profile')
# def display_user(user_id):
#     """Show profile.html template """
#     user = 
#     return render_template('profile.html', user=user)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')