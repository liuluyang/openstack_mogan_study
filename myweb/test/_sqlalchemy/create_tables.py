#coding:utf8
from myweb.test._sqlalchemy import db_api

if __name__ == '__main__':
    engine = db_api._engine
    db_api.make_models(engine)