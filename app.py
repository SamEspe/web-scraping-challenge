# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars 

# Create Flask app
app = Flask(__name__)

# Connect Flask to MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_scraping"
mongo = PyMongo(app)

# Make homepage route
@app.route("/")
def homepage():
    # Show contents of database
    display_data = mongo.db.scraped.find_one()
    # Send the information to the render template
    return render_template("index.html", data = display_data)

# Make /scrape route
@app.route("/scrape")
def scrape():
    # Create a database with the scraped dictionary in it
    scraped = mongo.db.scraped

    # Scrape the data
    data_scraped = scrape_mars.scrape()

    # Update the database
    scraped.update_one({}, {"$set": data_scraped}, upsert=True)

    # Redirect to the main page, send a message so we know it's successful
    return redirect("/", code=302)

# End part to make Flask work
if __name__ == "__main__":
    app.run(debug=True)


browser.close()