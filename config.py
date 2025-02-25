import os

class Config:
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:@localhost/tasks'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '265e9d1ef35635c99eed0ed3d95f7510')
    WTF_CSRF_ENABLED = True
