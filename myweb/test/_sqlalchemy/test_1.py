#coding:utf8

from oslo_db.sqlalchemy import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

class NovaBase(models.TimestampMixin,models.ModelBase):
    pass

Base = declarative_base(cls=NovaBase)
#只有继承此类时 Pic()才可进行dict()
class Pic(Base):
    __tablename__ = 'pics'
    name = 'pic'
    use = True
    id = Column(Integer, primary_key=True)

p = Pic()
p.update({'id':1})
print dict(p)

#{'created_at': None, 'updated_at': None, 'id': None}