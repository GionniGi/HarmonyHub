import datetime
from utils import validate_email, validate_password, validate_username, hash_password, get_ip, calculate_average
from models.user import User
from flask import request, jsonify

# Validate signup data
def validate_signup_data(username, email, password, confirm_password):

    # Import users collection
    from app import users

    # Check if all fields are filled
    if password != confirm_password:
        raise ValueError("Passwords do not match.")
    if not validate_password(password):
        raise ValueError("Password must be at least 8 characters long...")
    if not validate_email(email):
        raise ValueError("Email is not valid.")
    if not validate_username(username):
        raise ValueError("Username must be at least 3 characters long.")
    
    # Check if username or email already exists
    if users.find_one({'username': username}):
        raise ValueError("Username already taken.")
    if users.find_one({'email': email}):
        raise ValueError("Email already taken.")

# Signup user
def signup(username, email, password, confirm_password, first_name, last_name, birth_date, description, extroversion, friendliness, conscientiousness, openness, emotional_stability, ip_address):
    
    # Import users collection
    from app import users

    # Validate data
    validate_signup_data(username, email, password, confirm_password)

    # Create user and insert into database
    new_user = User(username, email, hash_password(password), first_name, last_name, birth_date, description, extroversion, friendliness, conscientiousness, openness, emotional_stability)
    user_object = vars(new_user)
    user_object['ipAddresses'] = [ip_address]
    user_object['lastAccessDate'] = datetime.datetime.utcnow()
    users.insert_one(user_object)
    return {"message": "User created successfully."}

# Post method for signup
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
