# heroku-app-with-postgres

This is a template for putting a python flask app on heroku with a postgres backend. This app queries the
database, then populates the html page with the retrieved data. Each significant file is explained below.

## Procfile
Lists the processes for heroku to spin up dynos for. This app uses gunicorn for web processes, and 
gunicorn uses the 'app' from the wsgi file. This is all under one command 'web'.

## data_upload_to_DB.ipynb
Contains the script for adding data to the postgres database. Reads the csv file, converts to a dataframe, 
then sends it to the database.

## main.py
Initializes the flask app. Holds all of the routes for the app and which python functions to run when. The 
app queries the database, converts the query to html, then renders the html template with the content.

## requirements.txt
gunicorn - for the web process in heroku
flask - webserver backend in python
pandas - for dataframes
sqlalchemy - for connecting/querying the database
psycopg2-binary - for connecting/querying the database
