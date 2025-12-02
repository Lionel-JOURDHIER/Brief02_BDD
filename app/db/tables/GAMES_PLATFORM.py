from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class GamesPlatforms(Base):
    __tablename__ = 'games_platforms'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    NA_sales = Column(Float(precision=2))
    EU_sales = Column(Float(precision=2))
    JP_sales = Column(Float(precision=2))
    other_sales = Column(Float(precision=2))
    global_sales =Column(Float(precision=2))
    
    # clé étrangère
    game_id = Column(Integer, ForeignKey('games.id'), nullable=True)
    game = relationship("Games", back_populates="game_platform") 

    platform_id = Column(Integer, ForeignKey('platforms.id'), nullable=True)
    platform = relationship("Platforms", back_populates="game_platform")