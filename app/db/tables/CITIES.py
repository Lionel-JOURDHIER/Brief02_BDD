from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cities(Base):
    __tablename__ = 'cities'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    city_name = Column(String)
   
    # clé étrangère
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship("Countries", back_populates="city")  

    # Relation to many
    city_pc_corresp = relationship("City_pc_corresps", back_populates="city")