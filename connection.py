import sqlalchemy as db
import os
from configparser import ConfigParser

from sqlalchemy.orm import sessionmaker

conf = ConfigParser()
conf.read(os.path.dirname(__file__)+'/config/conf.dev.ini')


def create_db_session():
    engine = db.create_engine(conf.get('DB', 'connection'))
    session = sessionmaker(bind=engine)
    return session()
