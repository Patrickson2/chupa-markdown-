# i am creating my first Flask application and also showcasing on the routing 
from flask import Flask # i am importing the flask class

@app.route('/') #this is the landing page of the application
def index(): #showcases that i am entering the home page 
    return '<h1>Welcome Home</h1>'

@app.route('/about') #this is the routing point for the application 
def about():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True) #easy way for running this Flask app