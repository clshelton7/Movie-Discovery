# pylint: disable=C0114, C0103, C0116, R1710, W0702, E1101
import os
import flask
from flask import Flask, render_template, request, json
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    logout_user,
    current_user,
)
from dotenv import load_dotenv, find_dotenv
from tmdb import get_movie_data, get_title_by_id
from wikimedia import getWiki
from models import db, MovieRatings, SiteUsers

load_dotenv(find_dotenv())


app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# point to heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# remove a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# key in .env generated randomly through a tutorial by flask
app.secret_key = os.getenv("SECRET")

if app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgres://"):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config[
        "SQLALCHEMY_DATABASE_URI"
    ].replace("postgres://", "postgresql://")

# Ikenna's method for preventing circular imports
db.init_app(app)

with app.app_context():
    db.create_all()

# flask-login has code that allows app and flask-login to communicate!
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return SiteUsers.query.get(int(user_id))


# react utility
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page, renders content in app.js
@bp.route("/profile", methods=["GET"])
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    if flask.request.method == "GET":
        return flask.render_template("index.html")


# main route allowing user to login
@app.route("/", methods=["GET", "POST"])
def login():
    """Log in functionality"""
    if flask.request.method == "POST":
        creds = request.form.get("username")
        # if there is a current user, they will be queried properly and logged in
        try:
            user = SiteUsers.query.filter_by(username=creds).first()
            login_user(user)
            return flask.redirect(flask.url_for("movies"))
        # if there is no user, they will be redirected to sign up
        except:
            flask.flash("Oops! That username does not exist. Please sign up below.")
            return render_template("signup.html")
    return render_template("login.html")


# user may signup if they do not have an account
# database additions if they sign up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Sign up functionality"""
    if flask.request.method == "POST":
        creds = request.form.get("newUsername")
        # checks whether or not username is blank
        if creds == "" or creds == " " or creds is None:
            flask.flash("Please enter a valid username! Username cannot be blank.")
            return flask.redirect(flask.url_for("signup"))
        # checks whether or not the username is already taken
        user = SiteUsers.query.filter_by(username=creds).first()
        if user is not None:
            flask.flash("That username is already taken!")
            return flask.redirect(flask.url_for("signup"))
        # adds a new user to the user db for viewing the site
        newUser = SiteUsers(username=creds)
        db.session.add(newUser)
        db.session.commit()
        flask.flash("You have signed up! Please log in.")
        return flask.redirect(flask.url_for("login"))
    return render_template("signup.html")


# user can log out of the website with flask libraries
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flask.flash("Logout successful!")
    return flask.redirect(flask.url_for("login"))


# main page for movie discovery and rating movies
# ratings are added to the page for viewing
@app.route("/movies", methods=["GET", "POST"])
@login_required
def movies():
    """Returns root endpoint HTML"""
    # checks whether or not username is blank
    if current_user != "" and current_user != " " and current_user is not None:
        # accesses information from apis
        movie_data = get_movie_data()
        movid = movie_data["id"]
        wiki_data = getWiki(movie_data["titles"])
        # initializes information for users and movies for return
        # lists are used for formatting display
        usersData = SiteUsers.query.all()
        ratingsData = MovieRatings.query.filter_by(movie_id=movid)
        ratingsList = []  # a list of list of ratings
        for rating in ratingsData:
            review = []  # each rating stored as a list

            # find user that left rating
            for user in usersData:
                if user.id == rating.user_id:
                    review.append(user.username)
            # add each rating element to list
            review.append(rating.rating)
            review.append(rating.comment)
            # add each user's rating to list of all ratings for the movie
            ratingsList.append(review)

        return render_template(
            "movies.html",
            movietitles=movie_data["titles"],
            moviegenres=movie_data["genres"],
            moviephotos=movie_data["photos"],
            movietags=movie_data["tags"],
            movielink=wiki_data["link"],
            ratings=ratingsList,
            user=current_user.username,
            movid=movid,
        )
    # if the user is not logged in, they are redirected to the login page
    return flask.redirect(flask.url_for("login"))


# route for handling rating additions
@app.route("/leaveRating", methods=["GET", "POST"])
@login_required
def rateMovie():
    # access information from the rating form
    movid = request.form.get("movieID")
    rating = request.form.get("userRating")
    comment = request.form.get("userComment")
    # create a new models entry object
    newRating = MovieRatings(
        movie_id=movid,
        rating=rating,
        comment=comment,
        user_id=current_user.id,
    )
    # add the object to the database
    db.session.add(newRating)
    db.session.commit()
    # user responsive
    flask.flash("Thanks for rating a movie!")
    return flask.redirect(flask.url_for("movies"))


# json response fetched in app.js for state variables
@app.route("/getreviews", methods=["GET", "POST"])
@login_required
def reviews():
    # access review information from the database
    # lists once again used for formatting data
    ratingsData = MovieRatings.query.filter_by(user_id=current_user.id)
    ratingsList = []
    commentsList = []
    titlesList = []
    # accessing each "attribute" of each review (iteration here)
    for rating in ratingsData:

        # find  movie title by id to return to React
        title = get_title_by_id(str(rating.movie_id))
        # add review information to lists
        titlesList.append(title)
        ratingsList.append(rating.rating)
        commentsList.append(rating.comment)

    # return jsonified lists response to App.js
    return flask.jsonify(
        name=current_user.username,
        ratings=ratingsList,
        comments=commentsList,
        titles=titlesList,
    )


# route for saving changes made to user ratings
@app.route("/save", methods=["GET", "POST"])
@login_required
def saveChanges():
    # access JSON review data from App.js, these are to be deleted from db
    deletedReviews = json.loads(flask.request.data)
    # iterate through JSON information of entries
    for items in deletedReviews:
        # setup to delete an entry by indexing response based on comment index
        moviesByComment = MovieRatings.query.filter_by(comment=deletedReviews[items][0])
        # iterate through reviews to be deleted from db
        for rating in moviesByComment:
            toDelete = MovieRatings.query.filter_by(id=rating.id).first()
            db.session.delete(toDelete)
            db.session.commit()

    return flask.redirect(flask.url_for("bp.index"))


app.register_blueprint(bp)

app.run()
