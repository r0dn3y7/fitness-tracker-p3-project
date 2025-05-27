from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"
    
