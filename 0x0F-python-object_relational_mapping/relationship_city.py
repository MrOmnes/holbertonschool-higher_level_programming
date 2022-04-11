#!/usr/bin/python3
"""Base Class Python"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """Base Class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = (Column(Integer, ForeignKey("states.id"), nullable=False))