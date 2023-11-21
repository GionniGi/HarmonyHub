from flask import render_template, request
from app import app
from utils import getIp
from models.user.user import User

# Add a signup route
@app.route('/signup', methods=['POST'])
def signup():
     try:
          # Get request data
          username = request.json['username']
          email = request.json['email']
          password = request.json['password']
          confirmPassword = request.json['confirmPassword']
          firstName = request.json['firstName']
          lastName = request.json['lastName']
          birthDate = request.json['birthDate']
          description = request.json['description']
          extroversion = request.json['extroversion']
          friendliness = request.json['friendliness']
          emotionalStability = request.json['emotionalStability']
          openness = request.json['openness']
          conscientiousness = request.json['conscientiousness']
          ipAddress = getIp(request)
          user = User()
          return user.signup(username, email, password, confirmPassword, firstName, lastName, birthDate, description, extroversion, friendliness, emotionalStability, openness, conscientiousness, ipAddress), render_template('login.html')
     except Exception as e:
          return str(e), 400
