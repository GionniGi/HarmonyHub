from utils import validate_email, validate_password, validate_username, hash_password
from models.user import User
from flask import url_for


# Validate signup data
def validate_signup_data(username, email, password, confirm_password):

    # Import users collection
    from app import db
    users = db['Users']

    # Check if username or email already exists
    if users.find_one({'username': username}):
        raise ValueError("Username already taken.")
    if users.find_one({'email': email}):
        raise ValueError("Email already taken.")

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

    # Create user and insert into database
    new_user = User(username, email, hash_password(password), first_name, last_name, birth_date, description)
    user_object = new_user.__dict__
    users.insert_one(user_object)

# Validate login data
def validate_login_data(username_email, password):

    # Import users collection
    from app import db
    users = db['Users']

    # Check if user exists
    if not users.find_one({$or: [{'username': username_email}, {'email': username_email}]}):
        signup_url = url_for('/user/signup/')
        error_message = f'User does not exist. Please register at <a href="{signup_url}">this page</a>.'
        raise ValueError(error_message)

    