import webapp2
import cgi
import jinja2
import os

from google.appengine.ext import db

# Models
class Movie(db.Model):
    title = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    watched = db.BooleanProperty(required=True)
    rating = db.RatingProperty(required=True)

    """docstring for ."""
    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
        
