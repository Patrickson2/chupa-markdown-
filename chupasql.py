# Flask-SQLAlchemy Simple Demo
# This file demonstrates basic Flask-SQLAlchemy usage with a simple User model

# Import necessary modules
from flask import Flask, request, jsonify  # Flask core components
from flask_sqlalchemy import SQLAlchemy    # SQLAlchemy ORM extension

# Create Flask application instance
app = Flask(__name__)

# ===== DATABASE CONFIGURATION =====
# Configure the database connection string
# SQLite is a lightweight, file-based database perfect for development
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple.db'  # Creates simple.db file

# Disable SQLAlchemy event system to save resources (recommended)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
# This creates the 'db' object that we'll use for all database operations
db = SQLAlchemy(app)

# ===== DATABASE MODEL =====
# Define a User model that inherits from db.Model
# This creates a 'user' table in the database
class User(db.Model):
    # Primary key column - auto-incrementing integer
    id = db.Column(db.Integer, primary_key=True)
    
    # Username column - string with max 80 chars, must be unique and not null
    username = db.Column(db.String(80), unique=True, nullable=False)
    
    # Email column - string with max 120 chars, must be unique and not null
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Method to convert User object to dictionary for JSON responses
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# ===== ROUTES (URL ENDPOINTS) =====

# Home route - simple welcome message
@app.route('/')
def home():
    return 'Simple Flask-SQLAlchemy Demo - Visit /users to see users'

# Users route - handles both GET (retrieve) and POST (create) requests
@app.route('/users', methods=['GET', 'POST'])
def users():
    # Handle POST request - create new user
    if request.method == 'POST':
        # Get JSON data from request body
        data = request.get_json()
        
        # Create new User instance with provided data
        user = User(username=data['username'], email=data['email'])
        
        # Add user to database session (staging area)
        db.session.add(user)
        
        # Commit the transaction to save to database
        db.session.commit()
        
        # Return the created user as JSON with 201 status code
        return jsonify(user.to_dict()), 201
    
    # Handle GET request - retrieve all users
    # Query all users from database
    users = User.query.all()
    
    # Convert list of User objects to list of dictionaries and return as JSON
    return jsonify([user.to_dict() for user in users])

# Individual user route - get specific user by ID
@app.route('/users/<int:user_id>')
def get_user(user_id):
    # Query user by ID, return 404 if not found
    user = User.query.get_or_404(user_id)
    
    # Return user data as JSON
    return jsonify(user.to_dict())

# ===== APPLICATION STARTUP =====
# This block runs only when the script is executed directly (not imported)
if __name__ == '__main__':
    # Create application context for database operations
    with app.app_context():
        # Create all database tables based on defined models
        # This creates the 'user' table if it doesn't exist
        db.create_all()
        
        # Create sample data for testing if no users exist
        if User.query.count() == 0:
            # Create a sample user
            sample_user = User(username='john_doe', email='john@example.com')
            
            # Add to session and commit to database
            db.session.add(sample_user)
            db.session.commit()
            
            print("Sample user created: john_doe")
    
    # Start the Flask development server
    # debug=True enables auto-reload and detailed error messages
    print("Starting Flask-SQLAlchemy Demo...")
    print("Visit: http://127.0.0.1:5000")
    app.run(debug=True)