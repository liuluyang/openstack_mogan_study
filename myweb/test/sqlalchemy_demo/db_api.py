#coding:utf8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from sqlalchemy import and_, or_
import time

from myweb.test.sqlalchemy_demo import db_models as models
from myweb.test.inbuild import hashlib_

# create engine link database
_engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/demo')

def get_session():
    session = sessionmaker(bind=_engine)
    return session()

class Connector(object):

    def __init__(self):
        pass

    def user_get(self, user_id):
        session = get_session()
        user = session.query(models.User).filter_by(id=user_id)
        #user = session.query(models.User).get(3)  #返回结果的第二项
        #return user
        return user.one()

    def transfer(self):
        session1 = get_session()
        session2 = get_session()

        u1 = session1.query(models.User).filter_by(id=1).with_lockmode('update').one()
        u2 = session2.query(models.User).filter_by(id=1).with_lockmode('update').one()

        u1.money -= 80
        #u2.money -= 50

        session1.add(u1)
        session1.commit()
        session1.close()

        u2.money -= 50
        session2.add(u2)
        session2.commit()
        session2.close()

    def create_user(self, values):
        session = get_session()
        user = models.User(**values)
        session.add(user)
        session.commit()

    def update_user(self, values, user_id):
        session = get_session()
        user = session.query(models.User).filter(models.User.id==user_id).with_lockmode('update').update(**values)
        session.add(user)
        session.commit()

    def delete_user(self, user_id):
        session = get_session()
        count = session.query(models.User).filter_by(id=user_id).delete()
        session.flush()
        print  session
        session.commit()
        print session

        return count

if __name__ == '__main__':
    c = Connector()

    #c.transfer()  #失败

    u = c.user_get(1)
    print u.name, u.money

    #c.create_user({'name':'xiaxia'})

    #c.update_user({'name':'xx'}, 1) #失败

    #print c.delete_user(5)