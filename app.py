from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)


if os.getenv("ENV") == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:    
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


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


@app.route('/',  methods=['GET', 'POST'])
def home():
    
    return render_template('home.html' )


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        original_url = request.form['original-url']
        # print(original_url)
        
        if original_url == '':
            return render_template('home.html', message='Please enter url to shotrten')
        
        if db.session.query(Url).filter(Url.original_url == original_url).count() == 0:
            data = Url(original_url, original_url)
            db.session.add(data)
            db.session.commit()

            return render_template('test.html')
        return render_template('home.html', message='Url already exists')


if __name__ == '__main__':
    app.run()