from utils import validate_email, validate_password, validate_username, hash_password, check_password
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies
from flask import url_for, jsonify


# Validate signup data
def validate_signup_data(username, email, password, confirm_password):

    # Import users collection
    from app import db
    users = db['Users']

    # Check if username or email already exists
    if users.find_one({'username': username}):
        raise ValueError("Username already taken.")
    if users.find_one({'email': email}):
        login_url = url_for('/user/login/')
        error_message = f'Email already taken. Please login at <a href="{login_url}">this page</a>.'
        raise ValueError(error_message)

    # Check if all fields are filled
    if password != confirm_password:
        raise ValueError("Passwords do not match.")
    if not validate_password(password):
        raise ValueError("Password must be at least 8 characters long...")
    if not validate_email(email):
        raise ValueError("Email is not valid.")
    if not validate_username(username):
        raise ValueError("Username must be at least 3 characters long.")

# Signup user
def signup(username, email, password, confirm_password, first_name, last_name, birth_date, description):

    # Import users collection
    from app import db
    users = db['Users']

    # Validate data
    validate_signup_data(username, email, password, confirm_password)

    # Create user object and insert into database
    user_object = {
        'username': username,
        'email': email,
        'password': hash_password(password),
        'first_name': first_name,
        'last_name': last_name,
        'birth_date': birth_date,
        'description': description
    }
    users.insert_one(user_object)

# Validate login data
def validate_login_data(username_email, password):

    # Import users collection
    from app import db
    users = db['Users']
    user_exists = users.find_one({'$or': [{'username': username_email}, {'email': username_email}]})
    error_message = 'Username or Password is incorrect.'

    # Check if user exists
    if user_exists is None:
        raise ValueError(error_message)
    
    # Check if password is correct
    if not check_password(password, user_exists.get('password')):
        raise ValueError(error_message)

# Login user
def login(username_email, password):

    # Import users collection
    from app import db
    users = db['Users']
    user_id = users.find_one({'$or': [{'username': username_email}, {'email': username_email}]}).get('_id')

    # Validate data
    validate_login_data(username_email, password)

    # Create access and refresh tokens
    access_token = create_access_token(identity=user_id)
    refresh_token = create_refresh_token(identity=user_id)

    # Return success message
    response = jsonify({"success": "User logged in successfully."})

    # Set cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response

# Logout user
def logout()