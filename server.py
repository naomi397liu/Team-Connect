

from flask import Flask, request, render_template, flash, redirect, session, jsonify
import crud
from jinja2 import StrictUndefined
from model import connect_to_db
import sys
import logging


app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def root():
    """Show homepage template."""
    return render_template('react.html')



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host='0.0.0.0')