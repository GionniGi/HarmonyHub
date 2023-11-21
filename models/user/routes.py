from flask import render_template, request, Blueprint, redirect
from utils import getIp
from models.user.user import User

# Initialize user blueprint
user_blueprint = Blueprint('user', __name__)

# Define routes
# Signup route
@user_blueprint.route('/signup/', methods=['GET', 'POST'])
def signup():
    try:
        data = request.json
        ip_address=getIp(request)

        response = User.signup(
            data.get('username', ''), 
            data.get('email', ''), 
            data.get('password', ''), 
            data.get('confirm_password', ''), 
            data.get('first_name', ''), 
            data.get('last_name', ''), 
            data.get('birth_date', ''), 
            data.get('description', ''), 
            data.get('extroversion', 0), 
            data.get('friendliness', 0), 
            data.get('emotional_stability', 0), 
            data.get('openness', 0),
            data.get('conscientiousness', 0),
            ip_address
        )
        return jsonify({"message": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
