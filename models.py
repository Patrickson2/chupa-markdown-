from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #this is a flask SQL extention just like the creation of an instance

# now i want to define a model class => which will be inherittting from db.model

class User(db.Model):# this indicates the database to be named as users
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    
### i will create classes while trying to make the e-commerce web

# class Post(db.Model): # this indicates the database to be named as posts
#     __tablename__ ='posts'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     content = db.Column(db.String)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # this is the foreign key constraint
#     user = db.relationship('User', backref=db.backref('posts', lazy=True))




