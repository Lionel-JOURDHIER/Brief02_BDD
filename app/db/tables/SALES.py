from sqlalchemy import Column, Integer, String, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Sales(Base):
    __tablename__ = 'sales'

    sales = Column(Float(precision=2))
    
    # clé étrangères
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Games", back_populates="sale") 

    region_id = Column(Integer, ForeignKey('regions.id'))
    region = relationship("Regions", back_populates="sale")

    # clé primaire à deux arguments
    __table_args__ = (
    PrimaryKeyConstraint('game_id', 'region_id', name='pk_sales'),
)