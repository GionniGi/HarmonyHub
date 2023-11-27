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
        # Get data from request
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_date = request.form['birth_date']
        description = request.form['description']
        extroversion = request.form['extroversion']
        friendliness = request.form['friendliness']
        conscientiousness = request.form['conscientiousness']
        openness = request.form['openness']
        emotional_stability = request.form['emotional_stability']
        ip_address = get_ip(request)

        # Signup user
        signup(username, email, password, confirm_password, first_name, last_name, birth_date, description, extroversion, friendliness, conscientiousness, openness, emotional_stability, ip_address)
        return jsonify({"success": "User created successfully."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        return jsonify({"error": "Missing field: " + str(e)}), 400