from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #this is a flask SQL extention just like the creation of an instance

# now i want to define a model class => which will be inherittting from db.model

class User(db.Model):# this indicates the database to be named as users
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    # One user can have as many Posts as they want
    posts = db.relationship('Post', back_populates='user')
    
    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}>'

### i will create classes while trying to make the e-commerce

class Post(db.Model): # this indicates the database to be named as posts
    __tablename__ ='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String(250))
    # now i want to create the SQLAlchemy relationship where one user has many posts.
    # and each foreign key links a post to a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    # each post belongs to one user
    user = db.relationship('User', back_populates='posts')




