#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='delete')
    else:
        name = ""
        cities = []

    # if getenv("HBNB_TYPE_STORAGE") == "db":
    @property
    def cities(self):
        cities_list = []
        all_cities = storage.all(City).values()
        for city in all_cities:
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
