#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        from models import storage
        objs = storage.all()
        cityl = []
        result = []

        for key in objs:
            var = key.replace('.', ' ')
            var = shlex.split(var)
            if (var[0] == 'City'):
                cityl.append(objs[key])

        for elem in cityl:
            if (elem.state_id == self.id):
                result.append(elem)

        return (result)
