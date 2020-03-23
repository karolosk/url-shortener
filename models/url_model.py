from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Url(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text())
    shorted_url = db.Column(db.Text())
    created = db.Column(db.Date())


    def __init__(self, original_url, shorted_url):
        self.original_url = original_url
        self.shorted_url = shorted_url
        self.created = date.today
