import os
import sqlalchemy as sa

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import orm
from admin.models import PlatformUser, Role, EnumRoles, Base


# region STARTUP
# environment variables
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

conn_url = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/" \
                   f"{POSTGRES_DB}"

engine = sa.create_engine(conn_url, echo=True)

Base.metadata.create_all(engine)

session = orm.Session(engine)

### add roles
roles = [Role(role=x.name) for x in EnumRoles]


# with session as s:

# endregion


app = Flask(__name__)

app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

admin = Admin(app, name='iva_dashboard', template_mode='bootstrap3')

admin.add_view(ModelView(PlatformUser, session))
admin.add_view(ModelView(Role, session))

app.run(host='0.0.0.0', port=8003, debug=True)


