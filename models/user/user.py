from flask import jsonify
from utils import validatePassword, validateEmail, validateUsername, hashPassword
import datetime

# Initialize User class
class User:
    
    # signup function
    def signup(self, username, email, password, confirmPassword, firstName, lastName, birthDate, description, extroversion, friendliness, emotionalStability, openness, conscientiousness, ipAddress):
        
        # Import userCollection from app.py
        from app import userCollection

        errors = []
        
        # Check if password and confirmPassword match
        if password != confirmPassword:
            errors.append('Passwords do not match')
        
        # Check if password is valid
        elif not validatePassword(password):
            errors.append('Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one number')
        
        # Check if email is valid
        elif not validateEmail(email):
            errors.append('Invalid email')
        
        # Check if username is valid
        elif not validateUsername(username):
            errors.append('Username must be at least 3 characters long and contain at least one letter and one number')
        
        # Check if username is already taken
        if userCollection.find_one({'username' : username}):
            errors.append('Username already taken')
        
        # Check if email is already taken
        elif userCollection.find_one({'email' : email}):
            errors.append('Email already taken')

        # Check if there are any errors
        if len(errors) > 0:
            return jsonify({'errors' : errors})
        
        # Hash password
        hashedPassword = hashPassword(password)

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
        userCollection.insert_one(userObject)
        return jsonify({'message' : 'User created successfully'})