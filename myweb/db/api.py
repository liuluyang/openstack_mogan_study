from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import exc

from myweb.db import models as db_models

import uuid

_ENGINE = None
_SESSION_MAKER = None

def get_engine():
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE

    _ENGINE = create_engine('sqlite:///myweb.db')
    db_models.Base.metadata.create_all(_ENGINE)
    return _ENGINE

def get_session_maker(engine):
    global _SESSION_MAKER
    if _SESSION_MAKER is not None:
        return _SESSION_MAKER

    _SESSION_MAKER = sessionmaker(bind=engine)
    return _SESSION_MAKER

def get_session():
    engine = get_engine()
    maker = get_session_maker(engine)
    session = maker()
    return session


class Connection(object):

    def __init__(self):
        pass

    def create_user(self, user_name):
        session = get_session()
        user_uuid = uuid.uuid4()
        #print type(user_uuid)
        new_user = db_models.User(id=str(user_uuid), name=user_name)
        session.add(new_user)

        session.commit()
        session.close()
        print 'create a new user success'

    def get_user(self, user_id):
        session = get_session()
        query = session.query(db_models.User).filter_by(id=user_id)
        try:
            user = query.one()
        except exc.NoResultFound as e:
            print e

        #return user

    def list_users(self):
        session = get_session()
        query = session.query(db_models.User)
        users = query.all()

        return users

    def update_user(self, user):
        pass

    def delete_user(self, user_name):
        session = get_session()
        query = session.query(db_models.User).filter_by(name=user_name)
        count = query.delete()
        print 'delete obj num: ',count
        session.commit()
        session.close()

    def create_book(self, book_name, user_id):
        session = get_session()
        book_uuid = uuid.uuid4()
        book = db_models.Book(id=str(book_uuid), name=book_name, user_id=user_id)
        #print book.name
        session.add(book)
        session.commit()
        session.close()
        print 'create a new book success'

    def book_list(self):
        session = get_session()
        query = session.query(db_models.Book)
        books = query.all()
        #print books
        return books





conn = Connection()
#print conn
#conn.create_user('bo')
#conn.create_book('jo','4aca4206-638d-4c33-8c99-00d91ff5778')

user_list = conn.list_users()
book_list = conn.book_list()

for user in user_list:
    print dict(user), user.name, user.id, user.books
    for i in user.books:
        print i.name
print '#'*20
for book in book_list:
    print book, book.name, book.user_id

print '#'*20
#print conn.get_user('4aca4206-638d-4c33-8c99-00d91ff5778a').name


conn.delete_user('bob')






