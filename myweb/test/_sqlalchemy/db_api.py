# coding:utf8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload
from sqlalchemy import and_
import time

from myweb.test._sqlalchemy import db_models as models
from myweb.test.inbuild import hashlib_

# create engine link database
_engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/user')


# create tables
def make_models(engine):
    models.Base.metadata.create_all(engine)


def get_session():
    engine = _engine
    session = sessionmaker(bind=engine)
    session = session()
    return session


def update(model, data):
    for key, val in data.items():
        if hasattr(model, key):
            setattr(model, key, val)
    return model


class Connection(object):
    def __init__(self):
        pass

    def user_create(self, user):
        session = get_session()
        model = models.User()

        password = hashlib_.passwd_md5(user.get('password'))
        user['password'] = password

        new_user = update(model, user)
        try:
            session.add(new_user)
            session.commit()
            print 'create a new user success'
        except Exception as e:
            print e

        return new_user

    def user_get_all(self):
        session = get_session()
        users = session.query(models.User)
        users = users.all()
        print 'get all users success'
        return users

    def user_delete(self, username):
        session = get_session()
        user_query = session.query(models.User).filter(
            models.User.username.in_(['lizhiwen']))
        # if user_query.delete()==1:
        # user_query.delete()
        # session.commit()
        # print 'ok'
        count = user_query.count()
        print 'delete user num is ', count
        user_query = user_query.all()
        return user_query

    def user_get_one(self, user_id):
        session = get_session()
        user_query = session.query(models.User).filter_by(
            id=user_id)  # .options(joinedload('articles'))

        # the_filter = [models.User.articles.has(title='python')]
        # user_query = user_query.filter(or_(*the_filter))

        try:
            user = user_query.one()
        except Exception as e:
            print e

        return user

    def article_create(self, article):
        session = get_session()
        model = models.Article()

        new_article = update(model, article)
        try:
            session.add(new_article)
            session.commit()
            print 'create an article success'
        except Exception as e:
            print e
        return new_article

    def article_get_all(self):
        session = get_session()
        articles = session.query(models.Article)
        articles = articles.all()
        print 'get all articles success'
        return articles

    def article_update(self, article, article_id):
        session = get_session()
        article_query = session.query(models.Article).filter_by(id=article_id)
        try:
            article_query = article_query.one()
            article = update(article_query, article)
            session.add(article)
            session.commit()
            print 'article update success'
            return article
        except Exception as e:
            print e

    def category_create(self, category):
        session = get_session()
        new_category = models.Category()

        new_category = update(new_category, category)
        session.add(new_category)
        session.commit()
        print 'create a category success'
        return new_category

    def category_get_all(self):
        session = get_session()
        categories = session.query(models.Category)
        categories = categories.all()
        print 'get all categories success'
        return categories

    def userinfo_create(self, userinfo_data):
        session = get_session()
        userinfo = models.UserInfo()

        new_userinfo = update(userinfo, userinfo_data)
        try:
            session.add(new_userinfo)
            session.commit()
        except Exception as e:
            print e

        return new_userinfo

    def userinfo_destroy(self, userinfo_id):
        session = get_session()
        userinfo_query = session.query(models.UserInfo).filter_by(
            id=userinfo_id)

        count = userinfo_query.delete()
        if count != 1:
            print 'delete not one'
        else:
            session.commit()

    def tag_get_all(self):
        session = get_session()
        tag_query = session.query(models.Tag).all()

        return tag_query

    def tag_destroy(self):
        session = get_session()
        # result = session.query(models.Tag).filter(models.Tag.name.in_(['1','on']))\
        # .delete(synchronize_session=False)
        result = session.query(models.Tag).filter(
            models.Tag.name == 'onfff').delete()
        # time.sleep(3)
        session.commit()
        # 操作结束 但未结束会话 且查询的字段没有索引时 会锁住整张表 无法进行其他操作

        print result

    def tag_update(self, values, tag_id):
        session = get_session()
        tag_query = session.query(models.Tag).filter_by(id=tag_id)

        try:
            tag_query = tag_query.one()
            # tag_query.name = 'g'
            # session.add(tag_query)
            # session.commit()
        except Exception as e:
            print e

        ref = update(tag_query, values)
        session.add(ref)
        session.commit()
        return ref

    def tag_create(self, tag_data):
        session = get_session()
        tag = models.Tag()

        new_tag = update(tag, tag_data)
        try:
            session.add(new_tag)
            session.commit()
        except Exception as e:
            print e

        return new_tag

    def lockmode_test(self):
        session1 = get_session()
        session2 = get_session()

        user1 = session1.query(models.User).filter_by(
            username='lizhi').with_lockmode('update').one()
        user2 = session2.query(models.User).filter_by(id=1).one()
        user2.username = 'jokef'
        session2.add(user2)
        session2.commit()

        # time.sleep(4)
        # session1.commit()
        # session2.commit()

    def add_tag_for_article(self, article_id, tag_id):
        session = get_session()
        article_tag = models.article_tag()
        query = session.query(models.article_tag).filter_by(
            article_id=article_id, tag_id=tag_id)
        if query:
            print 'tag is already in article!'
            return False
        new_article_tag = update(article_tag,
                                 {"article_id": article_id, "tag_id": tag_id})
        try:
            session.add(new_article_tag)
            session.commit()
            print 'add tag for article success'
        except Exception as e:
            print e

    def user_info_get_one(self, user_id):
        session = get_session()
        user_info = session.query(models.UserInfo).filter_by(id=user_id)
        try:
            user_info = user_info.one()
        except Exception as e:
            print e

        return user_info
