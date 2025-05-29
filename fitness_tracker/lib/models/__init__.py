from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///fitness_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

from . import user, workout, exercise
