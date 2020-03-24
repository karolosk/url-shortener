# Url-Stump

Url shortener application. Build with Flask and Postgres. 

Implementation is simple. We get the original url and convert it in a partial UUID. Then we generate an "endpoint" directly for the user to copy. This endpoint includes application's url and the partial UUID. This lead to a method which simply mathced the partial UUID in the database with its original URL and perform a redirection to the latter. 

## File structure

* db: Holds the db instance of SQLAlchemy
* errors: Custom errors/exceptions that are used in application
* models: Model of the entities that exist in database. At the moment only one is used.
* service: Since we do not use a repo layer, service are holding the queries that we need as well except the typical business logic.   
* templates: Typical template folder for Flask

## Other files

* Procfile: File used to deploy in Heroku
* .gitignore: Boilerplate gitignore file for Python projects
* static: Bootstrap is used, but we have some custom classes here that we use.
* Pipfile and Pipfile.lock are autogenerate from the pipenv which the the virual environment used for this application

## Using the app

Create a new folder for the project and initialize git and virual environment and activate the latter:

```console
$ mkdir url-stump
$ cd url-stump
$ git clone https://github.com/karolosk/url-shortener.git       
$ virtualenv venv 
$ source venv/bin/activate 
```

Install the needed dependecies in your virual environment:


```console
$ pip install -r requirements.txt
```

Finally run the application:

```console
$ python app.py # or python3 app.py if you have both versions
```

Application will start at port 5000


## Heroku deployment

Standard Heroku deployment, pulling from master on eah commit.

Application can be found here: 
[Url-Stump](https://url-stump.herokuapp.com/)
