from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Games(Base):
    __tablename__ = 'games'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    rank_game = Column(Integer)
    game_name = Column(String)
    NA_sales = Column(Float(precision=2))
    EU_sales = Column(Float(precision=2))
    JP_sales = Column(Float(precision=2))
    other_sales = Column(Float(precision=2))
    global_sales =Column(Float(precision=2))
    
    # clé étrangères
    release_year_id = Column(Integer, ForeignKey('release_years.id'), nullable=True)
    release_year = relationship("Release_years", back_populates="games") 

    publisher_id = Column(Integer, ForeignKey('publishers.id'), nullable=True)
    publisher = relationship("Publishers", back_populates="games")

    platform_id = Column(Integer, ForeignKey('platforms.id'), nullable=True)
    platform = relationship("Platforms", back_populates="games")  

    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=True)  
    genre = relationship("Genres", back_populates="games")

    # relation 0-N
    reviews = relationship("Reviews", back_populates="game")  


