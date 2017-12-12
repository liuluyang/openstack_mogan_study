
from oslo_db.sqlalchemy import models
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,ForeignKey,Text,schema,DateTime,Table,Boolean
from sqlalchemy import orm

from oslo_db.sqlalchemy import types as db_types

#_engine = create_engine('sqlite:///test.db')
#print _engine
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
    articles = orm.relationship(
        'Article'
    )
    userinfo = orm.relationship(
        'UserInfo',
        backref = 'user',
        uselist = False
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
        'User'
    )

class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = orm.relationship('Article', backref='category')


article_tag = Table(
    'article_tag',Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))

)

class Tag(Base):

    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(36), nullable=False)


class Server(Base):

    __tablename__ = 'servers'
    __table_args__ = (
        schema.UniqueConstraint('name',name='uniq_servers0name'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    flavor_id  = Column(Integer, nullable=True)

class Flavor(Base):

    __tablename__ = 'flavors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    servers = orm.relationship(
        Server,
        backref = orm.backref('flavor', uselist=False),
        foreign_keys=id,
        primaryjoin='Server.flavor_id == Flavor.id'
    )


class ComputeNode(Base):
    """Represents the compute nodes"""

    __tablename__ = 'compute_nodes'
    __table_args__ = (
        schema.UniqueConstraint(
            'node_uuid',name='uniq_compute_nodes0node_uuid'),
        table_args()
    )
    id = Column(Integer, primary_key=True)
    node_uuid = Column(String(36), nullable=False)
    cpus = Column(Integer, nullable=False)
    memory_mb = Column(Integer, nullable=False)
    hypervisor_type = Column(String(255), nullable=False)
    node_type = Column(String(255), nullable=False)
    used = Column(Boolean, default=False)
    availability_zone = Column(String(255), nullable=True)
    extra_specs = Column(db_types.JsonEncodedDict)

class ComputePort(Base):
    """Represents the compute ports"""

    __tablename__ = 'compute_ports'
    __table_args__ = (
        schema.UniqueConstraint(
            'port_uuid',name='uniq_compute_ports0port_uuid'),
        table_args()
    )
    id = Column(Integer, primary_key=True)
    port_uuid = Column(String(36), nullable=False)
    address = Column(String(18), nullable=False)
    port_type = Column(String(255), nullable=False)
    node_uuid = Column(String(36), nullable=False)
    extra_specs = Column(db_types.JsonEncodedDict)
    _node = orm.relationship(
        ComputeNode,
        backref = 'ports',
        foreign_keys=node_uuid,
        primaryjoin='ComputeNode.node_uuid == ComputePort.node_uuid'
    )

class ComputeDisk(Base):
    """Represents the compute disks"""

    __tablename__ = 'compute_disks'
    __table_args__ = (
        schema.UniqueConstraint(
            'disk_uuid',name='uniq_compute_disks0disk_uuid'),
        table_args()
    )

    id = Column(Integer, primary_key=True)
    disk_uuid = Column(String(36), nullable=False)
    size_gb = Column(Integer, nullable=False)
    disk_type = Column(String(255), nullable=False)
    node_uuid = Column(String(36), nullable=False)
    extra_specs = Column(db_types.JsonEncodedDict)
    _node = orm.relationship(
        ComputeNode,
        backref = 'disks',
        foreign_keys=node_uuid,
        primaryjoin='ComputeNode.node_uuid == ComputeDisk.node_uuid'
    )

class Test(Base):

    __tablename__ = 'test'
    __table_args__ = (
        #schema.UniqueConstraint(
            #'uuid','name',name='uniq'),
        table_args()
    )

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False,
                     onupdate='CASCADE')
    user = orm.relationship(
            User,
            backref=orm.backref('tests', cascade="all, delete-orphan",
                                passive_deletes=True),
            foreign_keys=user_id,
            primaryjoin='Test.user_id == User.id'
    )
