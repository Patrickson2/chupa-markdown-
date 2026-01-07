# FLASK
What is Flask:
- Flask is a lightweight WSGI(Web Server Gateway Interface) web application framework in Python. It is designed with simplicity and flexibility in mind, making it  easy to get started with web development. Flask provides the essential tools and features needed to build web applications, such as routing, request handling, and templating, while allowing developers to choose additional libraries and tools as needed.


## The HTTP VERBS USED 
This project uses the following HTTP verbs:
- GET: To retrieve data from the server.
- POST: To send new data to the server.
- PUT: To update existing data on the server.
- DELETE: To remove data from the server.
- PATCH: To make partial updates to existing data on the server.
- OPTIONS: To describe the communication options for the target resource.
- HEAD: To retrieve the headers for a resource without the body.
- TRACE: To perform a message loop-back test along the path to the target resource.
- CONNECT: To establish a tunnel to the server identified by the target resource.
These verbs are essential for RESTful API design and help in defining the actions that can be performed on the resources.  

## Start of in creation of Flask application on the web 
To start a project with Flask as the backend and React as the frontend, follow these steps  
1. Set up the Flask Backend:
   - Create a new directory for your project and navigate into it.
   - Create a virtual environment:
     ```bash
     pipenv install #for creation of (pipfiles dependencies in python)
     pipenv shell #enter virtual environment 
     ```
   - Install Flask:
     ```bash
     pipenv install Flask
     ```
   - Create a basic Flask app (app.py):
     ``` 
     check on the flask.py file for more description
        ```
    - Running the Flask app has two options:
        ```bash
        1)The process:
         - export FLASK_APP=Flask.py
         -export FLASK_RUN_PORT=5555 (specify on which port like ie.9000)
         -flask run
        2)Or directly run the app.py file:
            -python3 app.py (but first write this code(app.run(port=5555,debug=True)) on the bottom line of the (if__name))
        ```

### The requests hooks
Flask provides several request hooks that allow you to execute code at specific points during the request lifecycle. The most commonly used request hooks are:
1. `before_request`: This hook is executed before each request. It is often used for
    tasks such as authentication, logging, or setting up resources needed for the request.
    ```python
    @app.before_request
    def before_request_func():
         print("This function runs before each request.")
    ```
2. `after_request`: This hook is executed after each request, but before the response is sent to the client. It is commonly used for modifying the response or adding headers.
    ```python
    @app.after_request
    def after_request_func(response):
            print("This function runs after each request.")
            return response
        ```
3. `teardown_request`: This hook is executed after the response has been sent to the client. It is typically used for cleaning up resources, such as closing database connections.
    ```python
    @app.teardown_request
    def teardown_request_func(exception=None):
            print("This function runs after the request has been completed.")
    ```        
### Making of Application and Request Contexts
In Flask, the application context and request context are two important concepts that help manage the state of the application and handle incoming requests.
1. Application Context:
    - The application context is used to store information that is global to the application. It allows you to access certain objects, such as the current application instance and configuration settings, without having to pass them around
    explicitly.
    - You can push an application context using `app.app_context()` and access the current application  
    instance using `flask.current_app`.
2. Request Context:
    - The request context is specific to an individual HTTP request. It allows you to access request
    data, such as form data, query parameters, and headers, without having to pass the request
    object around explicitly.
    - You can push a request context using `app.test_request_context()` and access the current
    request using `flask.request`.
Both contexts are automatically managed by Flask during the handling of requests
, but you can also manually push and pop them when needed, such as during testing or when working with background tasks.
## FLASK-SQLALCHEMY
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy, which is
a popular SQL toolkit and Object-Relational Mapping (ORM) library for Python. Flask-SQLAlchemy simplifies the integration of SQLAlchemy with Flask applications, making it easier to work with databases.

### Features of Flask-SQLAlchemy:
1. Simplified Configuration: Flask-SQLAlchemy provides a simple way to configure the database connection
    using Flask's configuration system.
2. ORM Support: It allows you to define database models as Python classes, making it easier to work with
    database records as objects.
3. Querying: Flask-SQLAlchemy provides a high-level API for querying the database using
    SQLAlchemy's powerful query capabilities.
4. Migrations: It can be used in conjunction with Flask-Migrate to handle database migrations
5. Integration with Flask: Flask-SQLAlchemy seamlessly integrates with Flask's application context,
    making it easy to use within Flask routes and views.

### Basic Usage:
1. Install Flask-SQLAlchemy:
   ```bash
   pipenv install Flask-SQLAlchemy
         and then
   pipenv install Flask-migrate (which is for mapping the models to database tables) 
   ```
2. Set up Flask-SQLAlchemy in your Flask app:
    - For more infor check on app.py
3. Define your database models:
    - For more info check on models.py
- Create and manage the database:

4. After set up the database while running this in the terminal:
    ```bash
    flask db init # to get the migration file and this is done only once.
    flask db migrate -m "Initial migration." # to get the access to the database with its schema installed
    flask db upgrade head # so when creating a class of certain data this will be the final call for it to be added to the database.
    ```
5. Then enter the flask shell:
    ```bash
    flask shell
    >>> from your_app import User, Post, db
    >>> user1 #here you are creating the first user in database
    >>> post1 # creation of the first post
    >>> db.session.add(user1)  # you then add user to the database
    >>> db.session.add(post1)  # you then add Post to the database
    >>> db.session.commit()    # then commit changes so that they may appear to the database itself
    ```
6. To query the database:
    ```python
    >>> users = User.query.all()  # Get all users
    ```
7. To filter the database:
    ```python
    >>> user = User.query.filter_by(username='
    example').first()  # Get user with username 'example'
    ```
8. To filter_by() in the datavbase:
    ```python
    >>> posts = Post.query.filter(Post.title.like('%Flask%')).all()  # Get posts with 'Flask' in the title
    ```
9. To order_by() in the database:
    ```python
    >>> users = User.query.order_by(User.username.desc()).all()  # Get users ordered by username in descending order
    ```
10. To update records in the database:
    ```python
    >>> user = User.query.get(1)  # Get user with ID 1
    >>> user
    >>> user
    >>> db.session.commit()  # Commit the changes
    ```
11. To delete records from the database:
    ```python
    >>> user = User.query.get(1)  # Get user with ID 1
    >>> db.session.delete(user)  # Delete the user
    >>> db.session.commit()  # Commit the changes
    ```
12. To close the session:
    ```python
    >>> db.session.close()  # Close the session
    ```    
 - For more infor on the Database check on the instance folder containing the school.db
    
## We need the seed Data because 
Seeding data is the process of populating a database with initial or sample data. This is often done during development and testing to provide a realistic dataset for developers to work with. Seed data can help simulate real-world scenarios, test application functionality, and ensure that the application behaves as expected with different types of data.
### Why Seed Data is Important:
1. Testing: Seed data allows developers to test their applications with a variety of data scenarios,
    ensuring that the application can handle different inputs and edge cases.
2. Development: Having seed data makes it easier for developers to work on the application without
    needing to manually enter data each time they start the application.
3. Consistency: Seed data provides a consistent dataset for testing and development, making it easier
    to reproduce bugs and issues.
4. Demonstration: Seed data can be used to showcase the application's features and functionality to
    stakeholders or potential users.
### How to Seed Data:
1. Create a Seed Script: Write a script that populates the database with sample data.
2. Run the Seed Script: Execute the seed script to insert the data into the database.
3. Verify the Data: Check the database to ensure that the seed data has been inserted correctly

### Example of a Seed Script:
 - check on seed.py file.

### Running the Seed Script:
To run the seed script, use the following command in your terminal:
```bash
python seed.py
```
This will execute the seed script and populate the database with the initial data.

### Verifying the Seed Data:
After running the seed script, you can verify that the data has been inserted correctly by querying the
database or using a database management tool to inspect the tables and records.

## Also we can generate random data:
To generate random data for seeding purposes, you can use libraries such as Faker in Python. Faker allows you to create realistic fake data for various fields, such as names, addresses, phone numbers, and more.

### Installing Faker:
To install Faker, use the following command:
```bash
pipenv install Faker
```
### Example of Generating Random Data with Faker:
- Enter the Flask shell in the virtual Environment.
- Then import the Faker 
```python  
>>> from faker import Faker
>>> fake = Faker() 
>>> fake.name()  # So everytime we call the name method we can get a new random name.
'Kiptoo enok'
>>> fake.address()  # Generates a random address
'123 Main St, Springfield, IL 62701'
>>> fake.email()  # Generates a random email address
'enok@gmail.com'
>>> fake.phone_number()  # Generates a random phone number
'(555) 123-4567'
```
- Faker has a lot of random data generator functions that you can use but you can use the first three for examples.
### Using Faker in Seed Script:
You can integrate Faker into your seed script to generate random data for your database models. Here's an
example:
```python
from faker import Faker
fake = Faker()
for _ in range(10):
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        address=fake.address()
    )
    db.session.add(user)
db.session.commit()

This will create 10 random users with fake usernames, email addresses, and addresses, and add them to the database.
```
### How to Return a JSON(Javascript Object Notation) Response
- JSON is a is a data interchange format often used for transmitting data between a client and a server.JSON data is stored in a Python application as a String, but structured in a way that looks very similar to a JavaScript object.

- To return a JSON response from a Flask route, you can use the `jsonify` function provided by Flask. Here's an example of how to do this:

```python
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
```
- or the `make_response`:

```python
from flask import Flask, make_response, json
app = Flask(__name__)
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    response = make_response(json.dumps(data), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
if __name__ == '__main__':
    app.run(port=5555, debug=True)
```
### The SQLAlchemy Relationships and how they work.
- There is the Primary key in the data base which identifies a row in Datebase Table and the Foreign key which is the primary key to another table.
- In SQLAlchemy, relationships are defined using the `relationship()` function in conjunction with foreign keys. Relationships allow you to navigate between related objects in your database models.
Here's an example of how to define relationships in SQLAlchemy:

```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', back_populates='author')
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('Author', back_populates='books')
```
- The example above looks just the same as the one in models.py 

- In this example, we have two models: `Author` and `Book`. The `Author` model has a one-to-many relationship with the `Book` model, meaning that one author can have multiple books.
When you define relationships in SQLAlchemy, you can specify how the related objects should be loaded. The most common loading strategies are: 
1. Lazy Loading: This is the default loading strategy. Related objects are loaded only when they are accessed for the first time.
2. Eager Loading: Related objects are loaded immediately when the parent object is loaded. This
can be done using the `joined` or `subquery` loading strategies.
3. Dynamic Loading: This strategy returns a query object that can be further filtered or modified before
loading the related objects.

### Example of Using Relationships:
```python
# Creating an author and their books
author = Author(name='J.K. Rowling')
book1 = Book(title='Harry Potter and the Sorcerer\'s Stone', author=
author)
book2 = Book(title='Harry Potter and the Chamber of Secrets', author=author)
db.session.add(author)
db.session.add(book1)
db.session.add(book2)
db.session.commit()
# Querying an author and their books
author = Author.query.filter_by(name='J.K. Rowling').first()
for book in author.books:
    print(book.title)
```
- In this example, we create an author and two books associated with that author. We then
query the author and print the titles of their books using the relationship defined in the models.

### Many to many relationships:
- Many-to-many relationships are established using an association table that contains foreign keys referencing the primary keys of the related tables.
```python
association_table = db.Table('association',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
)
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', secondary=association_table, back_populates='students')
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    students = db.relationship('Student', secondary=association_table, back_populates='courses')
# after all this you migrate so to add data.
# then create an associate table and migrate then upgarde to add it to the database.

# The associate table code that is used to store many to many relations bten student and courses
students_courses = db.Table('students_courses', #this is the associate table 
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True))

 #Then enter the flask shell:
 from models import * # the (*) symbolizes many like everything 
    student1 = Student(name='Alice')
    student2 = Student(name='John')
    course1 = Course(title='Cyber sec')
    course2 = Course(title='Data Science')
    student1.courses.append(course1)  # Enroll Alice in Cyber sec
    student1.courses.append(course2)  # Enroll Alice in Data Science
    student2.courses.append(course1)  # Enroll John in Cyber sec
    # you can also do vice verser of all this by:
    course1.students.append(student1)  # Enroll Alice in Cyber sec
    db.session.add_all([student1, sudent2, course1, course2])
    db.session.commit()
```
- In this example, we have two models: `Student` and `Course`, with a
many-to-many relationship between them. The `association_table` is used to link students and courses.
- For more infor check on the models.py.


### Conclusion
- Relationships in SQLAlchemy provide a powerful way to navigate between related objects in your database models.
- By defining relationships using the `relationship()` function and foreign keys, you can easily access related data and perform complex queries involving multiple tables.
## FLASK-CORS
Flask-CORS is an extension for Flask that enables Cross-Origin Resource Sharing (CORS) support in your Flask applications. CORS is a security feature implemented by web browsers to restrict web pages from making requests to a different domain than the one that served the web page. This is known as the same-origin policy.
### Why Use Flask-CORS:
1. Cross-Origin Requests: If your Flask backend serves an API that is accessed by a frontend
application hosted on a different domain, you need to enable CORS to allow those requests.
2. Security: CORS helps protect your application from certain types of attacks, such as Cross
Site Request Forgery (CSRF).
### Installing Flask-CORS:
To install Flask-CORS, use the following command:
```bash
pipenv install Flask-CORS
```
### Basic Usage:
To use Flask-CORS in your Flask application, you need to import the `CORS`
class and initialize it with your Flask app. Here's an example:
```python
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
```
### Configuring CORS:
You can configure CORS to allow specific origins, methods, and headers. Here's an example of
how to do this:
```python
CORS(app, resources={r"/api/*": {"origins": "http://example
.com"}})  # Allow only requests from example.com to /api/ routes
```
### Conclusion:
Flask-CORS is a useful extension for enabling CORS support in your Flask applications. By
configuring CORS properly, you can ensure that your API can be accessed securely from different
domains while protecting your application from potential security risks.


