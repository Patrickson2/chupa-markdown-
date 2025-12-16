# i am creating my first Flask application and also showcasing on the routing 
from flask import Flask # i am importing the flask class

app = Flask(__name__) #this is the constructor of the flask class

# Routing - is the association of URLs and the code that should execute when a request comes in for that URL.
# The easiest way to define routes with Flask is through use of the (@app.route) decorator:

@app.route('/') #this is the routing point for the application 
def hello_world():
    return 'Hello, World!'