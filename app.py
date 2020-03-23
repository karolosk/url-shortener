from flask import Flask, render_template, request
from flask_sqlalchemy import session
import os


app = Flask(__name__)
from models.url_model import Url


@app.route('/',  methods=['GET', 'POST'])
def homme():
    print(request.method)
    # service = UrlService()
    # all = service.get_all()
    if request.method == 'GET':
        return render_template('home.html' ) #,all_urls = all)

    
    data = request.form['original-url']
    print(data)
    new = Url(data, data)

    session.add(new)
    session.commit()
    return render_template('home.html') #,all_urls = all) ,all_urls = all)

if __name__ == '__main__':
    app.run(debug=True)