import datetime
from utils import validate_email, validate_password, validate_username, hash_password
from models.user import User


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
def signup(username, email, password, confirm_password, first_name, last_name, birth_date, description, ip_address):

    # Import users collection
    from app import db
    users = db['Users']

    # Validate data
    validate_signup_data(username, email, password, confirm_password)

    # Create user and insert into database
    new_user = User(username, email, hash_password(password), first_name, last_name, birth_date, description)
    user_object = vars(new_user)
    user_object['ipAddresses'] = [ip_address]
    user_object['lastAccessDate'] = datetime.datetime.utcnow()
    print(user_object)
    users.insert_one(user_object)
