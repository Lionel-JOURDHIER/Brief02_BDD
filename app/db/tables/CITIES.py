from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from app.modules.encrypt import EncryptedString

class Cities(Base):
    __tablename__ = 'cities'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    city_name = Column(String)
   
    # clé étrangère
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=True)
    country = relationship("Countries", back_populates="cities")  

    # Relation to many
    city_pc_corresp = relationship("City_pc_corresps", back_populates="city")