
import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = (
        "mysql://"
        f"{os.getenv('DB_USERNAME')}"
        f":{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}"
        f"/{os.getenv('DATABASE_DEV')}"
    )


class TestConfig(Config):

    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = (
        "mysql://"
        f"{os.getenv('DB_USERNAME')}"
        f":{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}"
        f"/{os.getenv('DATABASE_TEST')}"
    )


class ProductionConfig(Config):

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = (
        "mysql://"
        f"{os.getenv('DB_USERNAME_PROD')}"
        f":{os.getenv('DB_PASSWORD_PROD')}"
        f"@{os.getenv('DB_HOST_PROD')}"
        f"/{os.getenv('DATABASE_PROD')}"
    )

config = {
    "default": DevelopmentConfig,
    "testing": TestConfig,
    "production": ProductionConfig
}
