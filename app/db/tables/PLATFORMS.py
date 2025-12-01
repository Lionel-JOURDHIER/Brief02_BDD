from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Platforms(Base):
    __tablename__ = 'platforms'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    platform_name = Column(String)
   
    # relation 0-N
    games = relationship("Games", back_populates="platform")  