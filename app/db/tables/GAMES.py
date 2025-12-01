from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Games(Base):
    __tablename__ = 'games'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True)  
    game_name = Column(String)
    NA_sales = Column(Float(precision=2))
    EU_sales = Column(Float(precision=2))
    JP_sales = Column(Float(precision=2))
    other_sales = Column(Float(precision=2))
    global_sales =Column(Float(precision=2))
    
    # clé étrangères
    release_year_id = Column(Integer, ForeignKey('release_years.id'))
    release_year = relationship("Release_years", back_populates="game") 

    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publisher = relationship("Publishers", back_populates="game")

    plateform_id = Column(Integer, ForeignKey('plateforms.id'))
    plateform = relationship("Plateforms", back_populates="game")  

    genre_id = Column(Integer, ForeignKey('genres.id'))  
    genre = relationship("Genres", back_populates="game")

    # relation 0-N
    review = relationship("Reviews", back_populates="game")  

    sale = relationship("Sales", back_populates="game")