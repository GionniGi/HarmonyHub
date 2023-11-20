from flask import Flask, jsonify
from utils import *

# Initialize User class
class User:
    
    # signup function
    def signup(self, username, email, password, confirmPassword, firstName, lastName, birthDate, description, extroversion, friendliness, emotionalStability, openness, conscientiousness, ipAddress)
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
