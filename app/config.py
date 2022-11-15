import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = 'ASFASFSFSAFSFSF' # os.getenv('SECRET_KEY') |
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Gopari@2022@localhost/monopoly'  # os.getenv('SQLALCHEMY_DATABASE_URI')
