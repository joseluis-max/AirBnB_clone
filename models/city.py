#!/usr/bin/python3
"""Class city
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City
        ===
        Attr:
        -----
            `state_id`: (string) id city - it will be State.id
            `name`: (string) City's name
    """
    state_id = ""
    name = ""
