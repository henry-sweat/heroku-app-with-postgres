from flask import Flask, render_template
import pandas as pd
import psycopg2
import os

app = Flask(__name__)
db_uri = os.environ['DB_URI']

@app.route('/')
def home():
   # create a new database connection by calling the connect() function
   con = psycopg2.connect(db_uri)
   # create a new cursor
   cur = con.cursor()
   # query
   query = 'SELECT * FROM drivers_by_season'
   # return results as df
   df = pd.read_sql(query, con)
   # convert df to html table
   table = df.to_html(index=False)
   #close connection
   if con is not None:
      con.close()

   return render_template('index.html',table=table)
