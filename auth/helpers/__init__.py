import os
import bcrypt
from models.User import User
from exceptions import (
    EmailAlreadyExistsException, 
    UserDoesNotExistsException,
    IncorrectPasswordException
)


salt = bcrypt.gensalt()
def generate_hash(password):
    # salt = os.environ.get("SALT_ROUNDS")
    # salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def insert_into_db(email, hash):
    if User.objects(email=email).first() is None:
        User(email=email, password=hash).save()
        user = User.objects(email=email).first()
        return {"email": user['email'], "password":user['password']}
    else:
        raise EmailAlreadyExistsException()

def get_user_from_db(email):
    user = User.objects(email=email).first() 
    if user is None:
        raise UserDoesNotExistsException()
    return user

def compare_password(email, password):
    user = get_user_from_db(email)
    db_hash = user['password'].encode('utf-8')
    hashed = generate_hash(password)
    paswd = password.encode('utf-8')
    if  bcrypt.checkpw(paswd, db_hash):
        return  {"email": user['email'], "password":user['password']}
    else:
        raise IncorrectPasswordException()
