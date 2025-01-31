import os
from dotenv import load_dotenv
from Database import Database
from Validator import email_validator, password_validator
from Model import User
from bcrypt import hashpw, gensalt, checkpw

load_dotenv()

db = Database(
    os.getenv('USERDB'),
    os.getenv('PASSWORD'),
    os.getenv('DATABASE'),
    os.getenv('HOST'),
    os.getenv('PORT')
)
db.connect()

class UserController:
    def login(self, username: str, password: str) -> bool:
        print(username, password)
        validator = email_validator(username)
        if validator:
            return validator
        validator = password_validator(password)
        if validator:                
            return validator
        user = db.session.query(User).filter(User.username == username).one_or_none()
        if not user:
            return 'Invalid User'
        if not checkpw(password.encode(), user.password.encode()):
            return 'Incorrect password'
        return 'Access granted...'
        
    def register_user(self, username: str, password, re_password: str) -> str:
        try:
            validator = email_validator(username)
            if validator:
                return validator
            validator = password_validator(password, re_password)
            if validator:                
                return validator
            exists_email = db.session.query(User).filter(User.username == username).one_or_none()
            if exists_email:
                return 'Email already registered'            
            password = hashpw(password.encode(), gensalt())            
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return 'User registered successfully'
        except Exception as e:
            return f'Error: Unable to save data: {e}'
            