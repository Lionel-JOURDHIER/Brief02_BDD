from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from app.modules.encrypt import EncryptedString

class Countries(Base):
    __tablename__ = 'countries'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    country_name = Column(String)
   
    # relation 0-N
    cities = relationship("Cities", back_populates="country")  