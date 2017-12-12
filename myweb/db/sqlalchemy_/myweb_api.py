#coding:utf8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
import time

#from myweb.test.inbuild import hashlib_
from myweb.db.sqlalchemy_ import models


_engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/myweb')

def make_models(engine):
    models.Base.metadata.create_all(engine)

#make_models(_engine)

def get_session():
    engine = _engine
    session = sessionmaker(bind=engine)
    session = session()
    return session


class Connection(object):

    def aggregate_get_all(self):
        session = get_session()
        agg = session.query(models.Aggregates)
        agg = agg.all()
        return agg

if __name__ == '__main__':
    c = Connection()
    agg_all = c.aggregate_get_all()
    for agg in agg_all:
        if agg.hosts:
            print agg.hosts[0].host_id