from flask import Flask, url_for, render_template, request
from models.schema import Schema
from service.url_service import UrlService

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def homme():
    print(request.method)
    service = UrlService()
    all = service.get_all()
    if request.method == 'GET':
        return render_template('home.html' ,all_urls = all)

    
    data = request.form['original-url']
    print(data)
    return render_template('home.html' ,all_urls = all)

if __name__ == "__main__":
    Schema()
    app.run(debug=True)