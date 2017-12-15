# coding:utf8
from oslo_db.sqlalchemy import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Text, schema, \
    DateTime, Table, Boolean
from sqlalchemy import orm
from oslo_db.sqlalchemy import types as db_types


class MoganBase(models.TimestampMixin,
        models.ModelBase):
    metadata = None

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d


Base = declarative_base(cls=MoganBase)

#https://segmentfault.com/a/1190000006949536
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(36), nullable=False)
    context = Column(Text)
    cate_id = Column(Integer, ForeignKey('categories.id'))
    tags = orm.relationship('Tag', secondary='article_tag', backref='articles')
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


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(36), nullable=False)
