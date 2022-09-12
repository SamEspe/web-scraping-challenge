# This will be my Flask app

# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
#from scrape_mars.py import scrape

# Create Flask app
app = Flask(__name__)

# Connect Flask to MongoDB

# Make homepage route
#@app.route("/")
#def homepage():

# Make /scrape route
#@app.route("/scrape")
#def scrape():

# End part to make Flask work
if __name__ == "__main__":
    app.run(debug=True)
