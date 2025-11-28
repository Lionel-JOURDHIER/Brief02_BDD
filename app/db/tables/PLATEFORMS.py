from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Plateforms(Base):
    __tablename__ = 'plateforms'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    plateform_name = Column(String)
   
    # relation 0-N
    game = relationship("Games", back_populates="plateform")  