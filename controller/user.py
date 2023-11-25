import datetime
from models.user import User
from app import users
from utils import validate_email, validate_password, validate_username, hash_password

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
