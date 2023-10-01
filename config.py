
import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = (
        "mysql://"
        f"{os.getenv('DB_USERNAME')}"
        f":{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}"
        f"/{os.getenv('DATABASE')}"
    )


config = {
    "default": DevelopmentConfig
}
