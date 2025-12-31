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
 Install Flask-SQLAlchemy:
   ```bash
   pipenv install Flask-SQLAlchemy
         and then
   pipenv install Flask-migrate (which is for mapping the models to database tables) 
   ```
- Set up Flask-SQLAlchemy in your Flask app:
   ```python
   ```
- After set up the database while running this in the terminal:
    ```bash
    flask db init # to get the migration file and this is done only once.
    flask db migrate -m "Initial migration." # to get the access to the database with its schema installed
    flask db upgrade head # so when creating a class of certain data this will be the final call for it to be added to the database.
    ```
- Then enter the flask shell:
    ```bash
    flask shell
    >>> from your_app import User, Post, db
    >>> user1 #here you are creating the first user in database
    >>> post1 # creation of the first post
    >>> db.session.add(user1)  # you then add user to the database
    >>> db.session.add(post1)  # you then add Post to the database
    >>> db.session.commit()    # then commit changes so that they may appear to the database itself
    ```

    



