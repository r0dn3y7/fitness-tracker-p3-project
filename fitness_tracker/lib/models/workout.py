from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="workouts")
    exercises = relationship("Exercise", back_populates="workout")

    def __repr__(self):
        return f"<Workout(id={self.id}, user_id={self.user_id})>"
