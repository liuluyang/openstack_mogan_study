#coding:utf8
from oslo_db.sqlalchemy import models
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, Text,\
    Table, schema, DateTime

class MoganBase(models.TimestampMixin, models.ModelBase):
    metadata = None

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d

Base = declarative_base(cls=MoganBase)

def table_args():
    print 'hello I am func table_args()'
    return {'mysql_engine': "InnoDB",
            'mysql_charset': "utf8"}


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myweb.test._sqlalchemy import db_models as models

#连接数据库
_engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/user')


#创建数据库表
def make_models(engine):
    models.Base.metadata.create_all(engine)
def create_tables(engine):
    models.Base.metadata.create_all(engine)

#创建会话
def get_session():
    engine = _engine
    session = sessionmaker(bind=engine)
    session = session()
    return session

def session():
    engine = _engine
    session = sessionmaker(bind=engine)
    session = session()
    return session

