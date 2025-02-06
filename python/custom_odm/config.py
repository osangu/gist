import os


class DatabaseConfig:
    NAME = os.environ['DATABASE_NAME']
    HOST = os.environ['DATABASE_HOST']
    PORT = os.environ['DATABASE_PORT']
    USER_NAME = os.environ['DATABASE_USER_NAME']
    USER_PASSWORD = os.environ['DATABASE_USER_PASSWORD']

    URL = f'mongodb://{USER_NAME}:{USER_PASSWORD}@{HOST}:{PORT}'
