### TEST DATABASE ###
import os
import unittest

from unittest import TestCase
from admin import PlatformUser, Roles
from admin.models import Base
from sqlalchemy import create_engine
from sqlalchemy import orm

# environment variables
POSTGRES_USER = 'pavelbeard'
POSTGRES_PASSWORD = 'Rt3$YiOO'
POSTGRES_DB = 'iva_db'
POSTGRES_HOST = '1.0.1.2'
POSTGRES_PORT = 5432


class DbInit:
    engine = create_engine(f"postgres+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/"
                           f"{POSTGRES_DB}")
    session = orm.Session(engine)


Base.metadata.create_all(DbInit.engine)


class TestDatabase(TestCase):
    def test_db(self):
        user = PlatformUser(username='borodinpa', firstname='pavel', middlename='andreevich',
                            lastname='borodin', email='borodinpa@css.rzd', password='Rt3$YiOO')

        with DbInit.session as session:
            session.add(user)
            session.commit()


if __name__ == '__main__':
    unittest.main()
