from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Genres(Base):
    __tablename__ = 'genres'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    genre_name = Column(String)
   
    # relation 0-N
    games = relationship("Games", back_populates="genre")  