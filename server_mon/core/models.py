import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class CPU(Base):
    __tablename__ = 'cpu_info'

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    cpu_count = sa.Column(sa.Integer, nullable=False)
    avg_load_1m = sa.Column(sa.Float, nullable=False)
    avg_load_5m = sa.Column(sa.Float, nullable=False)
    avg_load_15m = sa.Column(sa.Float, nullable=False)

    def __getitem__(self, item):
        return item

    def __repr__(self):
        return f"CPU()"
