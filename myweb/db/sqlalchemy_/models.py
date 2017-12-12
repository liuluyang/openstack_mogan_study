from oslo_db import options as db_options
from oslo_db.sqlalchemy import models
from oslo_db.sqlalchemy import types as db_types
import six.moves.urllib.parse as urlparse
from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Text
from sqlalchemy import orm
from sqlalchemy import schema, String, Integer
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

_engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/myweb')



#from mogan.common import paths
#from mogan.conf import CONF

#_DEFAULT_SQL_CONNECTION = 'sqlite:///' + paths.state_path_def('mogan.sqlite')


#db_options.set_defaults(CONF, connection=_DEFAULT_SQL_CONNECTION)


#def MediumText():
    #return Text().with_variant(MEDIUMTEXT(), 'mysql')


def table_args():
    #engine_name = urlparse.urlparse(CONF.database.connection).scheme
    #if engine_name == 'mysql':
        #return {'mysql_engine': CONF.database.mysql_engine,
                #'mysql_charset': "utf8"}
    #return None
    pass


class MoganBase(models.TimestampMixin,
                models.ModelBase):

    metadata = None

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d


Base = declarative_base(cls=MoganBase)

class Aggregates(Base):
    """Represents possible types for host_aggregates."""

    __tablename__ = 'aggregates'
    __table_args__ = (
        #schema.UniqueConstraint('uuid','name', name='uniq_host_aggregates0uuid0name'),
        table_args()
    )
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False, unique=True)
    name = Column(String(255), nullable=False, unique=True)
    availability_zone = Column(String(255), nullable=True)
    #host = Column(db_types.JsonEncodedList)
    #metadata = Column(db_types.JsonEncodedDict)


class AggregateHosts(Base):
    """Represents host associated aggregates."""

    __tablename__ = 'aggregate_hosts'
    __table_args__ = (
        schema.UniqueConstraint(
            'aggregate_uuid','host_id',
            name='uniq_aggregate_hosts0aggregate_uuid0host_id'
        ),
        table_args()
    )
    id = Column(Integer, primary_key=True)
    host_id = Column(String(36), nullable=False)
    aggregate_uuid = Column(String(36), nullable=False)
    aggregate = orm.relationship(
        Aggregates,
        backref='hosts',
        foreign_keys=aggregate_uuid,
        primaryjoin='AggregateHosts.aggregate_uuid'
                    ' == Aggregates.uuid')


class AggregateMetadata(Base):
    """Represents additional metadata as key/value pairs for an aggregate."""
    __tablename__ = 'aggregate_metadata'
    __table_args__ = (
        schema.UniqueConstraint(
            "aggregate_uuid", "key",
            name=("uniq_aggregate_metadata0"
                  "aggregate_uuid")
        ),
        table_args()
    )
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    value = Column(String(255))
    aggregate_uuid = Column(String(36), ForeignKey('aggregates.uuid'),
                         nullable=False)
    aggregate = orm.relationship(
        Aggregates,
        backref="metadata",
        foreign_keys=aggregate_uuid,
        primaryjoin='AggregateMetadata.aggregate_uuid'
                    '== Aggregates.uuid')


#Base.metadata.create_all(_engine)