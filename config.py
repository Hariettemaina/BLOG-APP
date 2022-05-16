import os 

from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = 'abcde'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://mhariette:67890j@localhost/jblog"
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
        
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://mhariette:67890j@localhost/jblog"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
}