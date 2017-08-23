from sqlalchemy import *
from migrate import *
from migrate.changeset import schema

meta_data = MetaData()

todo = Table('todo', meta_data,
       Column('id', Integer, primary_key=True, nullable=False),
       Column('title', String(length=128), nullable=False),
       Column('complete', Boolean(), nullable=False))

def upgrade(migrate_engine):
    meta_data.bind = migrate_engine
    meta_data.tables[u'todo'].create()

def downgrade(migrate_engine):
    meta_data.bind = migrate_engine
    meta_data.tables[u'todo'].drop()
