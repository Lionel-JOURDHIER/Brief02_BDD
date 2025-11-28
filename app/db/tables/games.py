from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Games(Base):
    __tablename__ = 'games'
    # clé primaire
    id = Column(Integer, primary_key=True)  
    game_name = Column(String)
    NA_sales = Column(Float(precision=2))
    EU_sales = Column(Float(precision=2))
    JP_sales = Column(Float(precision=2))
    other_sales = Column(Float(precision=2))
    global_sales =Column(Float(precision=2))
    
    # clé étrangère Release_years
    release_year_id = Column(Integer, ForeignKey('release_years.id'))
    release_year = relationship("Release_years", back_populates="games") 

    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publisher = relationship("Publisher", back_populates="games")

    plateform_id = Column(Integer, ForeignKey('plateforms.id'))
    plateform = relationship("Plateform", back_populates="games")  

    genre_id = Column(Integer, ForeignKey('genres.id'))  
    genre = relationship("Genres", back_populates="games")

    # relation 0-N
    reviews = relationship("Reviews", back_populates="games")  