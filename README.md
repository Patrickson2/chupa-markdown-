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
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install Flask:
     ```bash
     pipenv install Flask
     ```
   - Create a basic Flask app (app.py):
     ``` 
     check on the flask.py file for more description
        ```
    - Run the Flask app:
        ```bash
        flask run
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
    

