from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from fitness_tracker.lib.models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    workouts = relationship("Workout", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"
