from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fitness_tracker.lib.models import Base
from fitness_tracker.lib.models.user import User
from fitness_tracker.lib.models.workout import Workout
from fitness_tracker.lib.models.exercise import Exercise

engine = create_engine('sqlite:///fitness_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine) 
