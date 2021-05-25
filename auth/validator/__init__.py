import re
from exceptions import (
    EmptyPasswordException,
    EmptyEmailException,
    InvalidPasswordLengthException, 
    InvalidEmailException
)


regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def validate_password(password):
    if not password:
        raise EmptyPasswordException()
    password = password.strip()
    if len(password) < 6 or len(password) > 20:
        raise InvalidPasswordLengthException()

def validate_email(email):
    if not email:
        raise EmptyEmailException()
    if(re.search(regex, email)):
        print("Valid Email")
    else:
        raise InvalidEmailException()