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


def table_args():
    print 'hello I am func table_args()'
    return {'mysql_engine': "InnoDB",
            'mysql_charset': "utf8"}


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        schema.UniqueConstraint(
                'username',
                name='uniq_username0'
        ),
    )
    id = Column(Integer, primary_key=True)
    username = Column(String(36), nullable=False, unique=True)
    password = Column(String(36), nullable=False)
    email = Column(String(36), nullable=True)
    userinfo = orm.relationship(
            'UserInfo',
            backref='user',
            uselist=False  #一对一 如果有多个只会取一个 并进行提示并非异常
    )


class UserInfo(Base):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True)
    name = Column(String(36))
    phone = Column(String(36))
    address = Column(String(36))
    user_id = Column(Integer, ForeignKey('users.id'))


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(36), nullable=False)
    context = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    cate_id = Column(Integer, ForeignKey('categories.id'))
    tags = orm.relationship('Tag', secondary='article_tag', backref='articles')
    author = orm.relationship(
            'User',
            backref='articles',
            foreign_keys=user_id,
            primaryjoin='Article.user_id == User.id'
    )
    category = orm.relationship(
            'Category',
            backref='articles',
            foreign_keys=cate_id,
            primaryjoin='Article.cate_id == Category.id'
    )


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)


article_tag = Table(
        'article_tag', Base.metadata,
        Column('article_id', Integer, ForeignKey('articles.id')),
        Column('tag_id', Integer, ForeignKey('tags.id'))
)

'''
class Article_tag(Base):
    __tablename__ = 'article_tags'
    __table_args__ = (
        schema.UniqueConstraint(
            'article_id','tag_id',
            name='uniq_article_tag0'
        ),
    )
    article_id = Column(Integer, ForeignKey('articles.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
    article = orm.relationship(
            'Article',
            backref='article_tags',
            foreign_keys=article_id,
            primaryjoin='Article.id == Article_tag.article_id'
    )
    tag = orm.relationship(
            'Tag',
            backref='article_tags',
            foreign_keys=tag_id,
            primaryjoin='Tag.id == Article_tag.tag_id'
    )
'''
class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(36), nullable=False)
