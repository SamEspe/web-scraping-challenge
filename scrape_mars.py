# This is my code to scrape the websites

# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)

# Create scraping function
def scrape():

# Scraping for the Headline
    # Set URL for news site
    url_news = 'https://redplanetscience.com/'
    # Use Splinter to visit the website 
    browser.visit(url_news)
    # Make a Beautiful Soup object of the website via Splinter, look at the results
    html_news = browser.html
    soup_news = BeautifulSoup(html_news, 'html.parser')
    # Using the soup object, the headline is the class 'content_title' and the description is the class 'article_teaser_body'
    results = soup_news.find('div', class_='article_teaser_body')
    # Assign headline and description to variables
    headline = soup_news.find('div', class_ = 'content_title').get_text()
    description = soup_news.find('div', class_ = 'article_teaser_body').get_text()

# Scraping for the Featured Image
    # Load in new URL
    url_images = 'https://spaceimages-mars.com/'
    # Use Splinter to click the "Full Image" button
    browser.visit(url_images)
    # Explore the site with BeautifulSoup
    html_images = browser.html
    soup_images = BeautifulSoup(html_images, 'html.parser')
    # Save the image URL
    featured_image = soup_images.find('img', class_ = 'headerimage fade-in')
    image_extension = featured_image.get('src')
    image_full_url = 'https://spaceimages-mars.com/' + image_extension

# Scraping for Mars Facts
    # Load in new URL
    url_facts = 'https://galaxyfacts-mars.com/'
    browser.visit(url_facts)
    # Find facts table
    html_facts = browser.html
    soup_facts = BeautifulSoup(html_facts, 'html.parser')
    # Save data from facts table using Pandas
    tables = pd.read_html(url_facts)
    # Save the table I actually want
    mars_table = tables[1]
    # Construct an HTML table string, part 1: turn list into a dataframe
    mars_df = pd.DataFrame(mars_table)
    # Construct an HTML table string, part 2: turn dataframe into a table string
    mars_table_html = mars_df.to_html()

# Scraping for Mars Hemispheres
    # Create a dictionary to store the image information
    hemispheres = []
    # Load in new URL
    url_hemispheres = 'https://marshemispheres.com/'
    # Use Splinter to open the URL
    browser.visit(url_hemispheres)
    # Look at the site structure with Beautiful Soup
    hemispheres_html = browser.html
    soup_hemi = BeautifulSoup(hemispheres_html, 'html.parser')

    # Use Splinter to click on Cerberus picture
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
    # Get Cerberus Hemisphere
    cerberus_dict = {}
    cerberus_dict["title"] = "Cerberus Hemisphere Enhanced"
    cerberus_dict["image_url"] = browser.url
    # Navigate back to the main page
    browser.back()

    # Use Splinter to click on Schiaparelli picture
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    # Get Schiaparelli Hemisphere
    schiap_dict = {}
    schiap_dict["title"] = "Schiaparelli Hemisphere Enhanced"
    schiap_dict["image_url"] = browser.url
    # Navigate back to the main page
    browser.back()

    # Use Splinter to click on Syrtis Major picture
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    # Get Syrtis Major Hemisphere
    syrtis_dict = {}
    syrtis_dict["title"] = "Syrtis Major Hemisphere Enhanced"
    syrtis_dict["image_url"] = browser.url
    # Navigate back to the main page
    browser.back()

    # Use Splinter to click on Valles Marineris picture
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    # Get Valles Marineris Hemisphere
    valles_dict = {}
    valles_dict["title"] = "Valles Marineris Hemisphere Enhanced"
    valles_dict["image_url"] = browser.url

    # Append dictionaries to hemispheres list
    hemispheres.append(cerberus_dict)
    hemispheres.append(schiap_dict)
    hemispheres.append(syrtis_dict)
    hemispheres.append(valles_dict)

# Quit the browser
    browser.quit()

# Create the dictionary
    output = {"headline": headline, "description": description, "featured_image_url" : image_full_url, "mars_table_html" : mars_table_html, "hemispheres" : hemispheres}

# Return Stuff
    return output