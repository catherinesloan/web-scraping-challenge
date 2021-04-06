# STEPS TAKEN ... 
# Creating a route called /scrape that will import the scrape_mars.py script and call the scrape function.
# Storing the return value in Mongo as a Python dictionary.
# Creating a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.

## Taken from class 12.3 activity 10, ## commenting on any changes made

# from flask import Flask, render_template, redirect
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
## changing to scrape_mars as that is the name of my python file
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
## should it be mars_app??
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    ## Changing the name to mars
    mars = mongo.db.collection.find_one()

    # Return template and data
    # This is telling it to find a folder called template, and then a file called index.html, folder structure is important
    ## data_mars is what I'm going to call in index.html, this is the dictionary so will use dot notation look for {{ }}
    return render_templates("index.html", data_mars = mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    ## Calling the name of my file, scrape_mars, then the name of the function in that file, scrape
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    ## Changing to mars_data
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)