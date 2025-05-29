from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.__init__ import Base  # or wherever Base is defined

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    workouts = relationship("Workout", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"
