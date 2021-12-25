
import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps
from cs50 import SQL


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def getpercentage():
    """calculates the percentage progress"""
    
    db = SQL("sqlite:///progress.db")
    user_id = session["user_id"]
    counter = 0
    a = db.execute("SELECT a FROM users WHERE id = ?", user_id)[0]["a"]
    b = db.execute("SELECT b FROM users WHERE id = ?", user_id)[0]["b"]
    c = db.execute("SELECT c FROM users WHERE id = ?", user_id)[0]["c"]
    d = db.execute("SELECT d FROM users WHERE id = ?", user_id)[0]["d"]
    e = db.execute("SELECT e FROM users WHERE id = ?", user_id)[0]["e"]
        
    if a == 1:
        counter += 1
    if b == 1:
        counter += 1
    if c == 1:
        counter += 1
    if d == 1:
        counter += 1
    if e == 1:
        counter += 1
        
    if (counter == 0):
        percentage = 0
    if (counter == 1):
        percentage = 17
    if (counter == 2):
        percentage = 33
    if (counter == 3):
        percentage = 50
    if (counter == 4):
        percentage = 67
    if (counter == 5):
        percentage = 83
        
    return percentage

def getstep():
    """Gets next step"""
    percentage = getpercentage()
    if (percentage == 0):
        step = "appointment"
    if (percentage == 17):
        step = "test"
    if (percentage == 33):
        step = "test"
    if (percentage == 50):
        step = "simulator"
    if (percentage == 67):
        step = "circuit"
    if (percentage == 83):
        step = "tips"
        
    return step