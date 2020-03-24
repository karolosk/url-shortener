from flask import Flask, render_template, request, redirect, flash
import os
from dotenv import load_dotenv

from errors.custom_errors import NotValidUrlException, ShortedUrlNotFoundException
from db.db import db
from service.url_service import UrlService

load_dotenv()

app = Flask(__name__)

if os.getenv("ENV") == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.secret_key = str(os.getenv("SECRET_ΚΕΥ"))

else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.secret_key = str(os.getenv("SECRET_ΚΕΥ"))

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
            return render_template('home.html', message=os.getenv("HOST") + url_to_return.shorted_url)
        except NotValidUrlException:
            flash("Not valid url.")
            return render_template('home.html')


@app.route('/<shorted_url>')
def go_to_original_url(shorted_url):
    url_service = UrlService()
    try:
        actual_url = url_service.find_url(db.session, shorted_url)
        return redirect(actual_url)
    except ShortedUrlNotFoundException as e:
        return render_template('error.html', message=e.get_message())


if __name__ == '__main__':
    app.run()
