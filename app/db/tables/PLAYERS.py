import uuid
from sqlalchemy import Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship
from .base import Base
from app.modules.encrypt import EncryptedString

class Players(Base):
    __tablename__ = 'players'
    # clé primaire
    id = Column(Integer, primary_key=True, autoincrement=True) 

    uuid = Column(
        String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

    first_name = Column(String)
    last_name = Column(String)
    creation_date = Column(Date, server_default=func.current_date())
    
    # clé étrangères
    contact_id = Column(Integer, ForeignKey('contacts.id'), nullable=True)
    contact = relationship("Contacts", back_populates="player") 

    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=True)
    address = relationship("Addresses", back_populates="players")

    # relation 0-N
    reviews = relationship("Reviews", back_populates="player") 