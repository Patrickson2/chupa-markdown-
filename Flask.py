# i am creating my first Flask application and also showcasing on the routing 
from flask import Flask # i am importing the flask class

#create an instance of a class
app = Flask(__name__) #this is the constructor of the flask class

# Routing - is the association of URLs and the code that should execute when a request comes in for that URL.
# The easiest way to define routes with Flask is through use of the (@app.route) decorator:


@app.route('/') #this is the landing page of the application
def index(): #showcases that i am entering the home page 
    return '<h1>Welcome Home</h1>'

@app.route('/about') #this is the routing point for the application 
def about():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)