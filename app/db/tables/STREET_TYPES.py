from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base
from app.modules.encrypt import EncryptedString

class Street_types(Base):
    __tablename__ = 'street_types'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    street_type_name = Column(EncryptedString())
   
    # relation 0-N
    address = relationship("Addresses", back_populates="street_type")  