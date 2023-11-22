import datetime
from flask import jsonify
from utils import validate_email, validate_password, validate_username, hash_password

# Initialize User class
class User:
    
    # signup function
    def signup(self, username, email, password, confirmPassword, firstName, lastName, birthDate, description, extroversion, friendliness, emotionalStability, openness, conscientiousness, ipAddress):
        
        # Import userCollection from app.py
        from app import users
        
        # Check if password and confirmPassword match
        if password != confirmPassword:
            return jsonify({"message": "Passwords do not match."})
        
        # Check if password is valid
        if not validate_password(password):
            return jsonify({"message": "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number."})
        # Hash password
        hashedPassword = hash_password(password)
        
        # Check if email is valid
        if not validate_email(email):
            return jsonify({"message": "Email is not valid."})
        
        # Check if username is valid
        if not validate_username(username):
            return jsonify({"message": "Username must be at least 3 characters long."})    
        
        # Check if username is already taken
        if users.find_one({'username' : username}):
            return jsonify({"message": "Username already taken."})
        
        # Check if email is already taken
        if users.find_one({'email' : email}):
            return jsonify({"message": "Email already taken."})

        # Create user object
        userObject = {
            'username' : username,
            'email' : email,
            'password' : hashedPassword,
            'firstName' : firstName,
            'lastName' : lastName,
            'birthDate' : birthDate,
            'description' : description,
            'ratings' : {
                'extroversion' : extroversion,
                'friendliness' : friendliness,
                'emotionalStability' : emotionalStability,
                'openness' : openness,
                'conscientiousness' : conscientiousness
            },
            'ipAddresses' : [ipAddress],
            'lastAccessDate' : datetime.datetime.utcnow()
        }

        # Insert user object into database
        users.insert_one(userObject)
        return jsonify({"message": "User created successfully."})