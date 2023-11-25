import datetime
from utils import validate_email, validate_password, validate_username, hash_password, get_ip, calculate_average
from models.user import User
from app import users
from flask import request, jsonify


def signup(username, email, password, confirm_password, first_name, last_name, birth_date, description, extroversion, friendliness, conscientiousness, openness, emotional_stability, ip_address):
    # Validate input
    if password != confirm_password:
        return {"message": "Passwords do not match."}
    if not validate_password(password):
        return {"message": "Password must be at least 8 characters long and contain at least one digit, one uppercase letter, and one lowercase letter."}
    if not validate_email(email):
        return {"message": "Email is not valid."}
    if not validate_username(username):
        return {"message": "Username must be at least 3 characters long."}
    
    # Check if user already exists
    if users.find_one({'username': username}):
        return {"message": "Username already taken."}
    if users.find_one({'email': email}):
        return {"message": "Email already taken."}

    # Create user and insert into database
    new_user = User(username, email, hash_password(password), first_name, last_name, birth_date, description, extroversion, friendliness, conscientiousness, openness, emotional_stability)
    user_object = vars(new_user)
    user_object['ipAddresses'] = [ip_address]
    user_object['lastAccessDate'] = datetime.datetime.utcnow()
    users.insert_one(user_object)
    return {"message": "User created successfully."}

def signup_post():
    data = request.json
    if not data:
            return jsonify({'error': 'No data provided'}), 400
    ip_address = get_ip(request)
    response = signup(data.get('username', ''),
            data.get('email', ''),
            data.get('password', ''),
            data.get('confirm_password', ''),
            data.get('first_name', ''),
            data.get('last_name', ''),
            data.get('birth_date', ''),
            data.get('description', ''),
            calculate_average(
                data.get('extroversion1', 0),
                data.get('extroversion2', 0),
                data.get('extroversion3', 0)
                ),
            calculate_average(
                data.get('friendliness1', 0),
                data.get('friendliness2', 0),
                data.get('friendliness3', 0)
                ),
            calculate_average(
                data.get('conscientiousness1', 0),
                data.get('conscientiousness2', 0),
                data.get('conscientiousness3', 0)
                ),
            calculate_average(
                data.get('openess1', 0),
                data.get('openess2', 0),
                data.get('openess3', 0)
                ),
            calculate_average(
                data.get('stability1', 0),
                data.get('stability2', 0),
                data.get('stability3', 0)
                ),
            ip_address
        )
    return jsonify(response), 200

