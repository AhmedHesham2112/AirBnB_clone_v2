#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class amenity"""
    __tablename__ = "amenities"
    __table_args__ = {'mysql_charset': 'latin1'}
    name = Column(String(128), nullable=False)
