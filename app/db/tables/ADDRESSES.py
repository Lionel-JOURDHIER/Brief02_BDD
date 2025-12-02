from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from app.modules.encrypt import EncryptedString

class Addresses(Base):
    __tablename__ = 'addresses'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    address_number = Column(String)
    street_name = Column(String)
    
    # clé étrangères
    street_type_id = Column(Integer, ForeignKey('street_types.id'), nullable=True)
    street_type = relationship("Street_types", back_populates="address") 

    postal_code_id = Column(Integer, ForeignKey('postal_codes.id'), nullable=True)
    postal_code = relationship("Postal_codes", back_populates="address")

    # relation 0-N
    players = relationship("Players", back_populates="address") 