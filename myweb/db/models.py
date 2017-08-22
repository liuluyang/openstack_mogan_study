#coding:utf8

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext import declarative
from sqlalchemy import Index
from sqlalchemy.orm import relationship

from oslo_db.sqlalchemy import models

class MoganBase(#models.TimestampMixin,
                models.ModelBase):

    metadata = None

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d


Base = declarative.declarative_base(cls=MoganBase)

#Base = declarative.declarative_base()
'''
class User(Base):
    """User table"""

    __tablename__ = 'user'
    __table_args__ = (
        Index('ix_user_user_id','user_id'),
    )
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255))
'''

class User(Base):
    __tablename__ = 'user'

    id = Column(String(36), primary_key=True)
    name = Column(String(20))
    #sex = Column(String(10),default='girl')
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(36), ForeignKey('user.id'))