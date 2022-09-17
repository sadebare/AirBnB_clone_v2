#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ as env
import models


class State(BaseModel):
    """ State class 
    Attributes:
        __tablename__: table name
        name: input name
        cities: relation to cities table
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
