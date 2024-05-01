import os

from dotenv import load_dotenv


load_dotenv()


DB_POSTGRES_SCHEMA = os.environ.get("DB_POSTGRES_SCHEMA")
DB_POSTGRES_USERNAME = os.environ.get("DB_POSTGRES_USER")
DB_POSTGRES_PASSWORD = os.environ.get("DB_POSTGRES_PASSWORD")
DB_POSTGRES_HOST = os.environ.get("DB_POSTGRES_HOST")
DB_POSTGRES_PORT = os.environ.get("DB_POSTGRES_PORT")
DB_POSTGRES_NAME = os.environ.get("DB_POSTGRES_NAME")

IS_DB_ECHO_LOG = os.environ.get("IS_DB_ECHO_LOG")
DB_POOL_SIZE = os.environ.get("DB_POOL_SIZE")
DB_POOL_OVERFLOW = os.environ.get("DB_POOL_OVERFLOW")

JWT_MIN = os.environ.get("JWT_MIN")
JWT_SUBJECT = os.environ.get("JWT_SUBJECT")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRATION_TIME = os.environ.get("JWT_ACCESS_TOKEN_EXPIRATION_TIME")

HASHING_ALGORITHM = os.environ.get("HASHING_ALGORITHM")

ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS")
IS_ALLOWED_CREDENTIALS = os.environ.get("IS_ALLOWED_CREDENTIALS")
ALLOWED_METHODS = os.environ.get("ALLOWED_METHODS")
ALLOWED_HEADERS = os.environ.get("ALLOWED_HEADERS")

API_PREFIX = os.environ.get("API_PREFIX")
SERVER_HOST = os.environ.get("SERVER_HOST")
SERVER_PORT = os.environ.get("SERVER_PORT")
DEBUG = os.environ.get("DEBUG")
SERVER_WORKERS = os.environ.get("SERVER_WORKERS")
LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL")
