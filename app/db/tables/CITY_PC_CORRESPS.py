from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class City_pc_corresps(Base):
    __tablename__ = 'city_pc_corresps'
    # clé primaire
    id = Column(Integer, primary_key=True)  
   
    # clé étrangère
    postal_code_id = Column(Integer, ForeignKey('postal_codes.id'))
    postal_code = relationship("Postal_codes", back_populates="city_pc_corresp") 

    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship("Cities", back_populates="city_pc_corresp")
