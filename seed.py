# here is an example of a seed file 
# You can modify it to fit your application's needs
# This file is used to populate the database with initial data

from app import app 
from models import db, User, Post

with app.app_context():
    #here i want to create an list 
    users = [
        User(username='alice',
             email='alice@example.com',
             password='XXXXXXXXXXX'),
        User(username='XXX',
             email='bob@example.com',
             password='XXXXXXXXXXX')
    ]
    posts = [
        Post(title='First Post',
                content='This is the content of the first post.',
                user_id=1),
        Post(title='Second Post',
                content='This is the content of the second post.',
                user_id=2)
    ]
    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()
    print("Database seeded successfully!")
    