from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin #to_dict, serialize_rule, serialize_only 

db = SQLAlchemy() #this is a flask SQL extention just like the creation of an instance

students_courses = db.Table('students_courses', #this is the associate table 
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True))

# now i want to define a model class => which will be inherittting from db.model

class User(db.Model, SerializerMixin):# this indicates the database to be named as users
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    serialize_rules = ('-posts.user',)

    # One user can have as many Posts as they want
    posts = db.relationship('Post', back_populates='user')
    
    def __repr__(self):
        return f'<User {self.id}, {self.username}, {self.email}>'

### i will create classes while trying to make the e-commerce

class Post(db.Model, SerializerMixin): # this indicates the database to be named as posts
    __tablename__ ='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String(250))
    # now i want to create the SQLAlchemy relationship where one user has many posts.
    # and each foreign key links a post to a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    serialize_rules = ('-user.posts',)

    # each post belongs to one user
    user = db.relationship('User', back_populates='posts')

    def __repr__(self):
        return f'<Post {self.id}, {self.title}, {self.description}, {self.user_id}>'

# Now i want to add two models that will relate to the many-many relationships 
class Student(db.Model, SerializerMixin):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    serialize_rules = ('-courses.students',)

    # many to many relationship with course
    courses = db.relationship('Course', secondary=students_courses, back_populates='students')

class Course(db.Model, SerializerMixin):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)
    
    serialize_rules = ('-students.courses',)
    
    # many to many relationship with student
    students = db.relationship('Student', secondary=students_courses, back_populates='courses')

