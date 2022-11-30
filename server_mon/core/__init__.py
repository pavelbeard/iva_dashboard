from .decorators import static__init__


import os

from sqlalchemy import create_engine
from sqlalchemy import orm

DATABASE = os.getenv('POSTGRES_DB')
USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
HOST = os.getenv('POSTGRES_HOST')
PORT = os.getenv('POSTGRES_PORT')


class DbInit:
    @staticmethod
    def engine():
        engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine

    @staticmethod
    def session():
        session = orm.Session(DbInit.engine())
        return session
