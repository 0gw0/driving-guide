import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, getpercentage, getstep

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///progress.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show progress of user"""
    user_id = session["user_id"]
    
    if request.method =="POST":
        # checking if checkbox has been ticked
        if not request.form.get("checkbox"):
            return apology("click a checkbox to update")
            
        # updating database based on what has been clicked
        d = int(request.form.get("checkbox"))
        if d == 1:
            db.execute("UPDATE users SET a = True WHERE id = ?", user_id)
        if d == 2:
            db.execute("UPDATE users SET b = True WHERE id = ?", user_id)
        if d == 3:
            db.execute("UPDATE users SET c = True WHERE id = ?", user_id)
        if d == 4:
            db.execute("UPDATE users SET d = True WHERE id = ?", user_id)
        if d == 5:
            db.execute("UPDATE users SET e = True WHERE id = ?", user_id)
        
        # using functions created below we get percentage and next steps by checking the database
        percentage = getpercentage()
        step = getstep()
        
        return render_template("index.html", percentage=percentage, step=step)
        
    if request.method == "GET":
        # checks progress on progress.db
        percentage = getpercentage()
        step = getstep()
            
        return render_template("index.html", percentage=percentage, step=step)


@app.route("/appointment")
@login_required
def appointment():
    """redirect to e appointment for different locations"""
    return render_template("appointment.html")
    


@app.route("/test")
@login_required
def test():
    """Guide to important materials to prepare for tests"""
    user_id = session["user_id"]
    return render_template("test.html")


@app.route("/simulator")
@login_required
def simulator():
    """redirect to simulator"""
    return render_template("simulator.html")


@app.route("/circuit")
@login_required
def circuit():
    """redirect to circuit dates"""
    return render_template("circuit.html")
    

@app.route("/tips")
@login_required
def tips():
    """redirect to tips for practical driving test"""
    return render_template("tips.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        # check if symbol left blank then check if quote exsist
        if not symbol:
            return apology("symbol left blank")
        quote = lookup(symbol)
        if not quote:
            return apology("Sorry the stock does not exsist :(")
            
        return render_template("quoted.html", quote=quote, usd=usd)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
        
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        
        # check if username / password / confirmation empty
        if not username:
            return apology("username cannot be blank")
        if not password or not confirmation:
            return apology("password cannot be blank")
            
        # checking if password matches confirmation
        if password != confirmation:
            return apology("passwords do not match")
        
        # save username and hash if username is unique
        try:
            hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash)
            return render_template("login.html")
        except:
            return apology("username has already been taken")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)
    

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
