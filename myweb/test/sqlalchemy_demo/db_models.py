# coding:utf8
from oslo_db.sqlalchemy import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Text, schema, \
    DateTime, Table, Boolean
from sqlalchemy import orm
from oslo_db.sqlalchemy import types as db_types


class MoganBase(#models.TimestampMixin,
        models.ModelBase):
    metadata = None

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d


Base = declarative_base(cls=MoganBase)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    money = Column(Integer, default=0)


from sqlalchemy import create_engine

def _create_table():
    engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/demo')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    _create_table()
