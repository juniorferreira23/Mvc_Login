import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from Database import Database

load_dotenv()

db = Database(
    os.getenv('USERDB'),
    os.getenv('PASSWORD'),
    os.getenv('DATABASE'),
    os.getenv('HOST'),
    os.getenv('PORT')
)
db.connect()
db.base()

class User(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    
db.Base.metadata.create_all(db.engine)