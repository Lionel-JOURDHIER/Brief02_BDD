from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Publishers(Base):
    __tablename__ = 'publishers'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    publisher_name = Column(String)
   
    # relation 0-N
    game = relationship("Games", back_populates="publisher")  