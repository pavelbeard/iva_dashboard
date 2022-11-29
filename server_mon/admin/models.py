import enum

import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PlatformUser(Base):
    """
    Сущность пользователя админки и платформы IVA VIP
    uuid - UUID,\n
    username - Unicode(30),\n
    firstname - Unicode(30),\n
    middlename - - Unicode(30),\n
    lastname - - Unicode(30),\n
    email - EmailType,\n
    password - PasswordType(pbkd2_sha512)
    """
    __tablename__ = 'user'

    uuid = sa.Column(UUID, primary_key=True, nullable=False)
    username = sa.Column(sa.Unicode(30), nullable=False, unique=True)
    firstname = sa.Column(sa.Unicode(30), nullable=False)
    middlename = sa.Column(sa.Unicode(30), nullable=False)
    lastname = sa.Column(sa.Unicode(30), nullable=False)
    email = sa.Column(sau.EmailType, unique=True)
    password = sa.Column(sau.PasswordType(
        schemes=['pbkdf2_sha512']
    ), unique=False, nullable=False)

    def __getitem__(self, item):
        return item

    def __repr__(self):
        return f"PlatformUser(id={self.uuid}, username={self.username}," \
               f" firstname={self.firstname}, middlename={self.middlename}," \
               f" lastname={self.lastname}, email={self.email})"


class Roles(Base):
    class EnumRoles(enum.Enum):
        superadmin = 1
        admin = 2
        user = 3

    __tablename__ = 'roles'
    id = sa.Column(UUID, primary_key=True, nullable=False)
    role = sa.Column('value', sa.Enum(EnumRoles), nullable=False)
    user_id = sa.Column(UUID, sa.ForeignKey('user.id'))

