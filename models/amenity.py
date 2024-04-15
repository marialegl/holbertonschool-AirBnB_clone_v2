#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    name = Column(String(128), nullable=False)
    __tablename__ = "amenities"
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        overlaps="amenities"
    )
