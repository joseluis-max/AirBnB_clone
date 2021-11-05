#!/usr/bin/python3
"""Class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity

        Attr:
            name:(string) Amenity's name
    """
    city_id = ""
    name = ""
