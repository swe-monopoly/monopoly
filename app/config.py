import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = '97b4fcedf3ab35be74af34cd9c8c793d7c6101ec61fd23be050471dc78447fdb'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Gopari@2020@127.0.0.1/monopoly'
