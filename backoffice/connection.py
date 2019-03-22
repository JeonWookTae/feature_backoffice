from contextlib import contextmanager

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import os
from configparser import ConfigParser


conf = ConfigParser()
conf.read(os.path.dirname(__file__)+'/config/conf.dev.ini')


def create_db_session():
    engine = db.create_engine(conf.get('DB', 'connection'), echo=False)
    session = sessionmaker(bind=engine)
    return session()


@contextmanager
def get_session():
    session = create_db_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
