'''
Hotelify API Microservice
Authors: Sean T. Purvis, Brandon Revels, Sneha Racharla, Michael Whitney
'''
from flask import Flask
app = Flask(__name__)

'''
Index route that returns Hello World on a GET Request
'''
@app.route("/")
def hello():
    return "Hello World!"