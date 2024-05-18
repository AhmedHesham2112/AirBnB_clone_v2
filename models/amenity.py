#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity"""
    __table_args__ = {'mysql_charset': 'latin1'}
    name = ""
