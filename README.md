# Web Scraping Challenge
## Contributor: Sam Espe

### Overview
In this project, I created a Flask app that scrapes information from four different websites. This project includes a `screenshots` folder that holds the screenshots of my app, the Jupyter Notebook file `mission_to_mars.ipynb` in which I developed my scraping code, my Flask app `app.py`, my consolidated scraping code `scrape_mars.py`, and the template for my website (within the `templates` folder). 

#### Part 1: Scraping 
I used Splinter, Beautiful Soup, and Pandas in a Jupyter Notebook to develop my code to scrape data from the websites. I obtained the headline and description of the first article on the Mars News Site (`https://redplanetscience.com/`), the featured image from `https://spaceimages-mars.com/`, the table of Mars Facts from `https://galaxyfacts-mars.com/`, and the hemisphere images from `https://marshemispheres.com/`.

#### Part 2: MongoDB and Flask
I consolidated the Python code from the Jupyter Notebook into a stand-alone file `scrape_mars.py`, which contained a function `scrape_mars`. This function returns a dictionary with the key information that was scraped from the various websites. This dictionary was then put into a MongoDB database, where it was then accessed by my Flask app to create a website. I used Jinja2 to help create my HTML template.

Many thanks to TA Nick for helping me debug the intersection of MongoDB, Flask, and my Python scraping code. Thanks also to TA Chris for posting a very helpful hint on how to get Jinja2 to use the table HTML code.
