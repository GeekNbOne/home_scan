from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

basedir = os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:///' + os.path.join(basedir, 'data.sqlite'))


Base = declarative_base()

Base.metadata.create_all(engine)





