from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from fitness_tracker.lib.models import Base

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    reps = Column(Integer)
    workout_id = Column(Integer, ForeignKey('workouts.id'))

    workout = relationship("Workout", back_populates="exercises")

    def __repr__(self):
        return f"<Exercise(name='{self.name}', reps={self.reps})>"
