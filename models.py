# pylint: disable=C0114, C0103, C0115, E1101, R0903, C0115
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# model for ratings that can be added to movies for each user
class MovieRatings(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # id of the rating
    movie_id = db.Column(db.Integer, nullable=False)  # id of the movie being rated
    rating = db.Column(db.Integer, nullable=False)  # rating number value
    comment = db.Column(db.String(500), nullable=False)  # comment string value
    user_id = db.Column(db.Integer, nullable=False)  # id of user that left the rating

    def __repr__(self):
        return (
            # '<MovieRatings %r>' % self.rating
            "<MovieRatings %r>"
            % self.comment
        )


# model for users that can be used for logging into the site
class SiteUsers(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return "<SiteUsers %r>" % self.username
