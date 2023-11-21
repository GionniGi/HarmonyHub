import re
import bcrypt

# Function to validate password
def validatePassword(password):
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    else:
        return True
    
# Function to validate email
def validateEmail(email):
    if len(email) > 7:
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) != None:
            return True
    return False

# Function to validate username
def validateUsername(username):
    if len(username) < 3:
        return False
    elif not any(char.isalpha() for char in username):
        return False
    elif not any(char.isdigit() for char in username):
        return False
    else:
        return True
    
# Function to hash password
def hashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to check password
def checkPassword(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Function to get ip address
def getIp(request):
    return request.headers.get('X-Forwarded-For', request.remote_addr)