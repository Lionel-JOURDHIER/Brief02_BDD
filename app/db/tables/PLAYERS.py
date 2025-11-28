from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Players(Base):
    __tablename__ = 'players'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    first_name = Column(String)
    last_name = Column(String)
    creation_date = Column(Date)
    
    # clé étrangères
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship("Contacts", back_populates="player") 

    address_id = Column(Integer, ForeignKey('addresses.id'))
    address = relationship("Addresses", back_populates="player")

    # relation 0-N
    review = relationship("Reviews", back_populates="player") 