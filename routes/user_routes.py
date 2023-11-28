from flask import Blueprint, jsonify, render_template
from controller.user_controller import signup
from flask import request
from utils import get_ip

bp = Blueprint('user', __name__)

@bp.route('/signup/', methods=['GET'])
# Show signup page
def show_signup():
    return render_template('signup/signup.html')

@bp.route('/signup/', methods=['POST'])
# Signup user
def process_signup():
    try:
        data=request.get_json()

        # Get data from request
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        first_name = data['first_name']
        last_name = data['last_name']
        birth_date = data['birth_date']
        description = data['description']

        # Signup user
        signup(username, email, password, confirm_password, first_name, last_name, birth_date, description)

        return jsonify({"success": "User created successfully."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": "Missing field: " + str(e)}), 400