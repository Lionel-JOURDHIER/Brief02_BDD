from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Reviews(Base):
    __tablename__ = 'reviews'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    review_score = Column(Integer)
   
    # clé étrangère
    game_id = Column(Integer, ForeignKey('games.id'), nullable=True)
    game = relationship("Games", back_populates="reviews") 

    player_id = Column(Integer, ForeignKey('players.id'), nullable=True)
    player = relationship("Players", back_populates="reviews")
