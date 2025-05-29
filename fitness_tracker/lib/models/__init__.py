from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///fitness_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()
