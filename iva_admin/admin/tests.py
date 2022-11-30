### TEST DATABASE ###
import unittest
import uuid

import sqlalchemy as sa

from unittest import TestCase
from iva_admin.admin import PlatformUser, Role, EnumRoles
from sqlalchemy import orm
from iva_admin.admin.models import Base

# environment variables
POSTGRES_USER = 'pavelbeard'
POSTGRES_PASSWORD = 'Rt3*YiOO'
POSTGRES_DB = 'iva_db'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '8001'

conn_url = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/" \
                   f"{POSTGRES_DB}"
engine = sa.create_engine(conn_url, echo=True)
Base.metadata.create_all(engine)
session = orm.Session(engine)


class TestDatabase(TestCase):
    def test_db(self):
        user = PlatformUser(uuid=uuid.uuid4().hex, username='borodinpa', firstname='pavel', middlename='andreevich',
                            lastname='borodin', email='borodinpa@css.rzd', password='Rt3$YiOO')

        with session as s:
            s.add(user)
            s.commit()

    def test_get_user(self):
        query = sa.select(PlatformUser).where(PlatformUser.username == 'borodinpa')

        user = session.scalar(query)
        print(user)

    def test_create_roles(self):
        roles = [Role(uuid=uuid.uuid4().hex, role=EnumRoles.superadmin),
                 Role(uuid=uuid.uuid4().hex, role=EnumRoles.admin),
                 Role(uuid=uuid.uuid4().hex, role=EnumRoles.user)]

        with session as s:
            for role in roles:
                s.add(role)

            s.commit()

    def test_get_roles(self):
        query = sa.select(Role)

        objects = session.execute(query)

        for obj in objects:
            print(obj)

    def test_create_superadmin(self):
        result = [x for x in session.execute(sa.select(Role).where(Role.role == EnumRoles.superadmin))][0]

        role = [x for x in result][0]

        user = PlatformUser(uuid=uuid.uuid4().hex, username='borodinpa', firstname='pavel', middlename='andreevich',
                            lastname='borodin', email='borodinpa@css.rzd', password='Rt3$YiOO', role_uuid=role.uuid)

        with session as s:
            s.add(user)
            s.commit()

    def test_get_superadmin(self):
        query = sa.select(PlatformUser).where(PlatformUser.role_uuid == sa.select(Role.uuid).where(
            Role.role == EnumRoles.superadmin))

        result = session.execute(query)

        for r in result:
            print(r)
        pass

    def test_add_another_user(self):
        role = [x for x in session.execute(sa.select(Role.uuid).where(Role.role == EnumRoles.admin))][0]
        user = PlatformUser(uuid=uuid.uuid4().hex, username='andreevaa', firstname='andrey', middlename='andreevich',
                            lastname='andreev', email='andreevaa@css.rzd', password='Rt3%%&8989',
                            role_uuid=role.uuid)

        with session as s:
            s.add(user)
            s.commit()

        pass
    def test_add_another_user_2(self):
        role = [x for x in session.execute(sa.select(Role.uuid).where(Role.role == EnumRoles.admin))][0]
        user = PlatformUser(uuid=uuid.uuid4().hex, username='nikolaevvn', firstname='valentin', middlename='nikloaevich',
                            lastname='nikolaev', email='nikolaevvn@css.rzd', password='Rt3%@@8989',
                            role_uuid=sa.select(Role.uuid).where(Role.role == EnumRoles.superadmin))

        with session as s:
            s.add(user)
            s.commit()

        pass

    def test_get_all_users(self):
        x = session.query(PlatformUser.username, PlatformUser.firstname, PlatformUser.lastname, Role.role).join(Role).filter(
            Role.uuid == sa.select(Role.uuid).where(Role.role == EnumRoles.superadmin)).all()
        # result = [x for x in x for x in x]
        print(x)


if __name__ == '__main__':
    unittest.main()
