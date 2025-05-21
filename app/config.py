import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')