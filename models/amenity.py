#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv


class Amenity(BaseModel):
    """amenties """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)
    else:
        name = ""
