import re


def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    return False


def validate_password(password):
    regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    if re.fullmatch(regex, password):
        return True
    return False

def validate_name(name):
    regex = r'^[A-Za-z\s]+$'
    if re.fullmatch(regex, name):
        return True
    return False

state = {
    'email': '',
    'password': '',
    'first_name': '',
    'last_name': '',
    'message': 'Please Log In',
    'isAuth': False
}