from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Publishers(Base):
    __tablename__ = 'publishers'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    publisher_name = Column(String)
   
    # relation 0-N
    game = relationship("Games", back_populates="publisher")  