import datetime
from utils import validate_email, validate_password, validate_username, hash_password

# Initialize User class
class User:
    
    # signup function
    def signup(self, username, email, password, confirm_password, first_name, last_name, birth_date, description, extroversion, friendliness, emotional_stability, openness, conscientiousness, ip_address):
        
        # Import userCollection from app.py
        from app import users
        
        # Check if password and confirmPassword match
        if password != confirm_password:
            return {"message": "Passwords do not match."}
        
        # Check if password is valid
        if not validate_password(password):
            return {"message": "Password must be at least 8 characters long and contain at least one digit, one uppercase letter, and one lowercase letter."}
        # Hash password
        hashed_password = hash_password(password)
        
        # Check if email is valid
        if not validate_email(email):
            return {"message": "Email is not valid."}
        # Check if username is valid
        if not validate_username(username):
            return {"message": "Username must be at least 3 characters long."}
        
        # Check if username is already taken
        if users.find_one({'username' : username}):
            return {"message": "Username already taken."}
        
        # Check if email is already taken
        if users.find_one({'email' : email}):
            return {"message": "Email already taken."}

        # Create user object
        user_object = {
            'username' : username,
            'email' : email,
            'password' : hashed_password,
            'firstName' : first_name,
            'lastName' : last_name,
            'birthDate' : birth_date,
            'description' : description,
            'ratings' : {
                'extroversion' : extroversion,
                'friendliness' : friendliness,
                'emotionalStability' : emotional_stability,
                'openness' : openness,
                'conscientiousness' : conscientiousness
            },
            'ipAddresses' : [ip_address],
            'lastAccessDate' : datetime.datetime.utcnow()
        }

        # Insert user object into database
        users.insert_one(user_object)
        return {"message": "User created successfully."}