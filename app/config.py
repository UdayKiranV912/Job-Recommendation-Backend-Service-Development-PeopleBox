import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://localhost/Job-Recommendation-Backend-Service-Development-PeopleBox')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

