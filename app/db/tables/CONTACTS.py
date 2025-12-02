from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from app.modules.encrypt import EncryptedString

class Contacts(Base):
    __tablename__ = 'contacts'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    email = Column(String)
    mobile_phone = Column(String)
   
    # relation 0-N
    player = relationship("Players", back_populates="contact")  