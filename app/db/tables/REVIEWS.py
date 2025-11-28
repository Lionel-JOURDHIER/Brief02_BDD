from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Reviews(Base):
    __tablename__ = 'reviews'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    review_score = Column(Integer)
   
    # clé étrangère
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Games", back_populates="review") 

    player_id = Column(Integer, ForeignKey('publishers.id'))
    player = relationship("Players", back_populates="review")
