from datetime import date
from db.db import db


class Url(db.Model):

    __tablename__ = 'url'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.Text())
    shorted_url = db.Column(db.Text())
    created = db.Column(db.Date())

    def __init__(self, original_url, shorted_url):
        self.original_url = original_url
        self.shorted_url = shorted_url
        self.created = date.today()
