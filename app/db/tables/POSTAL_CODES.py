from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Postal_codes(Base):
    __tablename__ = 'postal_codes'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    postal_code_value = Column(String)
   
    # relation 0-N
    address = relationship("Addresses", back_populates="postal_code")  

    # Relation to many
    city_pc_corresp = relationship("City_pc_corresps", back_populates="postal_code")