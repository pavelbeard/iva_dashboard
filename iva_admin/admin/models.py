import uuid
import enum
import sqlalchemy as sa
import sqlalchemy_utils as sau

from sqlalchemy import orm
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class EnumRoles(enum.Enum):
    """Роли пользователей"""
    superadmin = 1
    admin = 2
    user = 3


class Role(Base):
    """
    Роль пользователя админки и платформы IVA VIP
    uuid - UUID PK,\n
    role - Value,\n
    user_id - FK(user.uuid)
    """
    __tablename__ = 'role'
    uuid = sa.Column(UUID(as_uuid=True), primary_key=True, unique=True,
                     default=uuid.uuid4().hex)
    role = sa.Column('value', sa.Enum(EnumRoles), nullable=False, unique=True)
    # department = sa.Column('value', sa.Enum(EnumNS), nullable=False, unique=True)

    users = orm.relationship('PlatformUser', backref='role')

    def __getitem__(self, item):
        return item

    def __repr__(self):
        return f"Role(uuid={self.uuid}, role={self.role})"


class PlatformUser(Base):
    """
    Сущность пользователя админки и платформы IVA VIP
    uuid - UUID PK,\n
    username - Unicode(30),\n
    firstname - Unicode(30),\n
    middlename - - Unicode(30),\n
    lastname - - Unicode(30),\n
    email - EmailType,\n
    password - PasswordType(pbkd2_sha512)
    """
    __tablename__ = 'user'

    uuid = sa.Column(UUID(as_uuid=True), primary_key=True, unique=True,
                     default=uuid.uuid4().hex)
    username = sa.Column(sa.Unicode(30), nullable=False, unique=True)
    firstname = sa.Column(sa.Unicode(30), nullable=False)
    middlename = sa.Column(sa.Unicode(30), nullable=False)
    lastname = sa.Column(sa.Unicode(30), nullable=False)
    email = sa.Column(sau.EmailType, unique=True)
    password = sa.Column(sau.PasswordType(
        schemes=['pbkdf2_sha512']
    ), unique=False, nullable=False)
    role_uuid = sa.Column(UUID(as_uuid=True), sa.ForeignKey('role.uuid', ondelete='no action'))

    def __getitem__(self, item):
        return item

    def __repr__(self):
        return f"PlatformUser(id={self.uuid}, username={self.username}," \
               f" firstname={self.firstname}, middlename={self.middlename}," \
               f" lastname={self.lastname}, email={self.email})"
