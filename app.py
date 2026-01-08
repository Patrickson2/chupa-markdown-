# i am creating my first Flask application and also showcasing on the routing 
from flask import Flask # i am importing the flask class
from flask_migrate import Migrate #this is the migration instance
# from models import db #this is the database instance
from models import * #i want to import everything


#create an instance of a class
app = Flask(__name__) #this is the constructor of the flask class

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db' #this is the configuration of the database

migrate = Migrate(app, db)

# now we initialize flask app to use db
db.init_app(app)

# Routing - is the association of URLs and the code that should execute when a request comes in for that URL.
# The easiest way to define routes with Flask is through use of the (@app.route) decorator:


@app.route('/') #this is the landing page of the application
def index(): #showcases that i am entering the home page 
    return '<h1>Welcome Home</h1>'

@app.route('/about') #this is the routing point for the application 
def about():
    return '<h1>Hello, World!</h1>'

@app.route('/users')
def get_all_users():
    return [user.to_dict() for user in User.query.all()]    

if __name__ == '__main__':
    app.run(port=5555, debug=True) #easy way for running this Flask app