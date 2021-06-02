# web-scraping-challenge

## Mission to Mars

**If cloning this repository ...
**1. Activate local environment in terminal
**2. Run 'python app.py' 
**3. Follow local host link to view the app in your browser**

## Task:
To build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Ouput:
**Part 1 - Scraping**
1. Created a [Jupyter Notebook](mission_to_mars.ipynb) to complete initial scraping using:
   - BeautifulSoup
   - Pandas
   - Requests/Splinter

**Part 2 - MongoDB and Flask Application**
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped in Part 1
1. Converted the Jupyter notebook into a Python script, [scrape_mars.py](https://github.com/catherinesloan/web-scraping-challenge/blob/main/missions_to_mars/app/scrape_mars.py) 
2. Function called 'scrape' executes all of the scraping code and returns one Python dictionary containing all of the scraped data
3. Created a route called '/scrape' that imports the scrape_mars.py script and calls the scrape function
4. Stored the return value in Mongo as a Python dictionary
5. Created a route in [Flask app](https://github.com/catherinesloan/web-scraping-challenge/blob/main/missions_to_mars/app/app.py) that queries the Mongo database and passes the mars data into a HTML template to display the data
6. The [HTML file](https://github.com/catherinesloan/web-scraping-challenge/blob/main/missions_to_mars/app/templates/index.html)takes the mars data dictionary and displays all of the data in the appropriate HTML elements


