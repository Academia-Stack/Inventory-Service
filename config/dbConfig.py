import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# TODO: Load environment variables from .env file
load_dotenv()

class DBConfig:
    HOST = os.getenv("DB_HOST_NAME")
    PORT = os.getenv("DB_PORT")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    @staticmethod
    def get_db_uri():
        return (
            f"postgresql://{quote_plus(DBConfig.USER)}:{quote_plus(DBConfig.PASSWORD)}"
            f"@{DBConfig.HOST}:{DBConfig.PORT}/{DBConfig.DB_NAME}"
        )