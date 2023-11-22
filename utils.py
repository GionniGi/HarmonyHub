"""
This module provides utility functions for password validation, email validation,
username validation, password hashing, password checking, and IP retrieval.
"""

import re
import bcrypt

def validate_password(password):
    """
    Validates a password based on the following criteria:
    - Length should be at least 8 characters
    - Should contain at least one digit
    - Should contain at least one uppercase letter
    - Should contain at least one lowercase letter
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

def validate_email(email):
    """
    Validates an email address using regular expression pattern matching.
    """
    if len(email) > 7:
        if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None:
            return True
    return False

def validate_username(username):
    """
    Validates a username based on the length requirement.
    """
    if len(username) < 3:
        return False
    return True

def hash_password(password):
    """
    Hashes a password using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    """
    Checks if a password matches the hashed password using bcrypt.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def get_ip(request):
    """
    Retrieves the IP address from the request headers or remote address.
    """
    return request.headers.get('X-Forwarded-For', request.remote_addr)
