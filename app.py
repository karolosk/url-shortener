from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

from errors.not_valid_url_error import NotValidUrlException
from db.db import db
from service.url_service import UrlService

load_dotenv()

app = Flask(__name__)

if os.getenv("ENV") == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/',  methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        url_to_stump = request.form['original-url']

        if url_to_stump == '':
            return render_template('home.html',
                                   message='Please enter url to shotrten')

        url_service = UrlService()
        try:
            url_to_return = url_service.get_or_create(db.session, url_to_stump)
            return render_template('home.html', message=url_to_return.shorted_url)
        except NotValidUrlException:
            return render_template('home.html', message='Not valid url')


if __name__ == '__main__':
    app.run()
