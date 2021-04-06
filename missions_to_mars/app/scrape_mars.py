# STEPS TAKEN ...
# Converting the jupyter notebook 'mission_to_mars' into a python file, removed comments
# Created a scrape function to return one Python dictionary containing all of the scraped data

# Import library
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#  this will execute all of the scraping code from below to return Python dictionary, 'data', containing all of the scraped data.
def scrape():
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_p = mars_title_paragraph(broswer)

    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "feature_image": feature_image(browser),
        "facts": facts_table(),
        "hemispheres": hemisphere_image_title(browser)
    }
    browser.quit()
    return data

# the next 4 functions are the code from mission_to_mars.ipynb
# naming the function, passing in the argument of browser if it requires it
# remembering to return the scraped data you need at the end of the function
# Mish suggests to create different functions (unlike class 12.2 activity 10) as different url's used
# use these to define the function for scrape all above
def mars_title_paragraph(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    item_list = soup.select_one("ul.item_list")
    news_title = item_list.find("div", class_= "content_title").text
    news_p = item_list.find("div", class_= "article_teaser_body").text

    return news_title, news_p

def feature_image(browser):
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars3.jpg'

    return featured_image_url


def facts_table():
    df = pd.read_html('https://space-facts.com/mars/')
    mars_df = df[0]
    mars_df.columns = ['Description', 'Mars']
    mars_df.set_index('Description', inplace = True)
    mars_facts = mars_df.to_html() 

    return mars_facts

def hemisphere_image_title(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemisphere_image_urls = []
    title_links = browser.find_by_css("a.product-item h3")

    for x in range(len(title_links)):
        hemispheres = {}
        browser.find_by_css("a.product-item h3")[x].click()
        title = browser.find_by_css("h2.title").text
        hemispheres["title"] = title
        image_url = browser.links.find_by_text('Sample').first
        hemispheres['img_url'] = image_url['href']
        hemisphere_image_urls.append(hemispheres)
        browser.visit(url)

    return hemisphere_image_urls
