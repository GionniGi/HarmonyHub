from flask import render_template, request, Blueprint
from utils import getIp
from models.user.user import User

# Initialize user blueprint
user_blueprint = Blueprint('user', __name__)

# Define routes
# Signup route
@user_blueprint.route('/user/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    # Add a signup route
    try:
        # Get request data
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        confirm_password = request.json['confirmPassword']
        first_name = request.json['firstName']
        last_name = request.json['lastName']
        birth_date = request.json['birthDate']
        description = request.json['description']
        extroversion = request.json['extroversion']
        friendliness = request.json['friendliness']
        emotional_stability = request.json['emotionalStability']
        openness = request.json['openness']
        conscientiousness = request.json['conscientiousness']
        ip_address = getIp(request)          
        user = User()
        response = user.signup(username, email, password, confirm_password, first_name, last_name, birth_date, description, extroversion, friendliness, emotional_stability, openness, conscientiousness, ip_address)
        if 'errors' in response.json:
            return response
        return render_template('login.html')
    except Exception as e:
        return str(e), 400
