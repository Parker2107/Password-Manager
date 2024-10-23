import os

#from cs50 import SQL
from sql import SQL
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, g
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db=SQL("sqlite:///passwords.db")
"""def get_db():
    #Opens a new database connection if there is none yet for the current application context.
    if 'db' not in g:
        g.db = sqlite3.connect('passwords.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    #Closes the database again at the end of the request.
    db = g.pop('db', None)
    if db is not None:
        db.close()"""

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    #db = get_db()
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    passwords = db.execute("SELECT website, userID, password FROM passwords WHERE user_id = ? ORDER BY website DESC", user_id)
    #print(passwords)
    return render_template("index.html", passwords=passwords)

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    #db = get_db()
    """Create New Password"""
    if request.method=="GET":

        return render_template("create.html")

    if request.method=="POST":

        user_id=session["user_id"]
        website = request.form.get("website")
        username = request.form.get("username")
        pass_old = request.form.get("pass1")
        pass_new = request.form.get("pass2")

        '''print(website)
        print(username)
        print(pass_old)
        print(pass_new)'''

        if len(pass_old) <= 6:
            return apology("Password must be more than 6 characters", 400)
        if len(pass_old) >= 20:
            return apology("Password must be less than 20 characters", 400)
        if pass_old!=pass_new:
            return apology("Passwords don't match", 400)

        db.execute("INSERT INTO passwords (user_id, website, UserID, Password) VALUES (?, ?, ?, ?)",user_id, website, username, pass_old)

        return redirect ("/")
@app.route("/delete",methods=["GET", "POST"])
@login_required
def delete():
    #db = get_db()
    if request.method=="GET":

        return render_template("delete.html")

    if request.method=="POST":

        user_id=session["user_id"]
        website = request.form.get("website")
        username = request.form.get("username")
        pass_old = request.form.get("pass1")
        count=0
        passes = db.execute("SELECT Website, UserID, Password FROM passwords WHERE user_id = ?", user_id)
        print (type(passes[0]["Website"]))
        for i in range(0, len(passes)):
            if website==passes[i]["Website"] and username==passes[i]["UserID"] and pass_old==passes[i]["Password"]:
                db.execute("DELETE FROM passwords WHERE UserID = ? AND Password = ? AND Website = ?", username, pass_old, website)
                count=0
                break
            else:
                count=1
        if count>=1:
            return apology("Entered Login not Found", 400)
        return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    #db = get_db()
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

@app.route("/register", methods=["GET", "POST"])
def register():
    #db = get_db()
    """Register user"""
    if request.method == "POST":
        # Ensure username was submitted
        username = request.form.get("username")
        if not username:
            return apology("must provide username", 400)

        # Ensure password was submitted
        password = request.form.get("password")
        if not password:
            return apology("must provide password", 400)

        # Ensure passwords match
        if password != request.form.get("confirmation"):
            return apology("passwords don't match", 400)

        # Check if username is already taken
        existing_user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if existing_user:
            return apology("username already taken", 400)

        # Hash the password and insert the user into the users table
        password_hash = generate_password_hash(password, method='pbkdf2', salt_length=16)

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password_hash)

        return redirect("/login")  # Redirect user to login page after successful registration

    else:
        return render_template("register.html")
