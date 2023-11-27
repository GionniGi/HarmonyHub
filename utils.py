import re
import bcrypt
import math

# Validates a password
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

# Validates an email address using regular expression pattern matching.    
def validate_email(email):
    if len(email) > 7:
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None:
            return True
    return False

# Validates a username based on the length requirement.    
def validate_username(username):
    if len(username) < 3:
        return False
    return True

# Hashes a password using bcrypt.    
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Checks if a password matches the hashed password using bcrypt.    
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Retrieves the IP address from the request headers or remote address.    
def get_ip(request):
    return request.headers.get('X-Forwarded-For', request.remote_addr)

# Calculates the average of a list of scores and rounds it up.    
def calculate_average(*scores):
    if not scores:
        return 0
    average_score = sum(scores) / len(scores)
    return math.ceil(average_score)
