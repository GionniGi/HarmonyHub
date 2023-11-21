from flask import jsonify
from utils import validatePassword, validateEmail, validateUsername, hashPassword
from app import user
import datetime

# Initialize User class
class User:
    
    # signup function
    def signup(self, username, email, password, confirmPassword, firstName, lastName, birthDate, description, extroversion, friendliness, emotionalStability, openness, conscientiousness, ipAddress):
        
        # Check if password and confirmPassword match
        if password != confirmPassword:
            return jsonify({'message' : 'Passwords do not match'})
        
        # Check if password is valid
        elif not validatePassword(password):
            return jsonify({'message' : 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number.'})
        
        # Check if email is valid
        elif not validateEmail(email):
            return jsonify({'message' : 'Email is not valid'})
        
        # Check if username is valid
        elif not validateUsername(username):
            return jsonify({'message' : 'Username must be at least 4 characters long.'})
        
        # Check if username is already taken
        if user.find_one({'username' : username}):
            return jsonify({'message' : 'Username already taken'})
        
        # Check if email is already taken
        elif user.find_one({'email' : email}):
            return jsonify({'message' : 'Email already taken'})
        
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
        user.insert_one(userObject)
        return jsonify({'message' : 'User created successfully'})