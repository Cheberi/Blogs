import os 

class Config:
    SECRET_KEY = os.environ.get("dcadb4817ccfc31f2a0b")
    SQLALCHEMY_DATABASE_URI = os.getenv("postgresql+psycopg2://cheberi:Meshack011@localhost/blogs")
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("postgresql+psycopg2://cheberi:Meshack011@localhost/blogs")

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://cheberi:Meshack011@localhost/blogs"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://cheberi:Meshack011@localhost/blogs"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}