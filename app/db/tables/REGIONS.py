from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Regions(Base):
    __tablename__ = 'regions'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    region_name = Column(String)
   
    # relation 0-N
    sale = relationship("Sales", back_populates="region")  