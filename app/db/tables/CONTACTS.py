from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Contacts(Base):
    __tablename__ = 'contacts'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    email = Column(String)
    mobile_phone = Column(String)
   
    # relation 0-N
    player = relationship("Players", back_populates="contact")  