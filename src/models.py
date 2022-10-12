import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    def __init__(self, user_name, user_password):
        self.name = user_name
        self.email = user_email
        self.password = user_password


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    imagen = Column(String(250), nullable=False)    
    height = Column(String(50), nullable=False) 
    age = Column(String(50), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    image = Column(String(250), nullable=False)  
    terrain = Column(String(50), nullable=False)   
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)

    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character")

    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet")

    user_id = Column(Integer, ForeignKey("user.id"))           
    user = relationship("User")

    def favorite_char(self, char_id):
        self.character_id = char_id 
    
    def favorite_plan(self, planet_id):
        self.planet_id = planet_id 
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')