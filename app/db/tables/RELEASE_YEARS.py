from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Release_years(Base):
    __tablename__ = 'release_years'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    release_year = Column(String)
   
    # relation 0-N
    game = relationship("Games", back_populates="release_year")  