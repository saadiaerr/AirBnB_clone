#!/usr/bin/python3

""" define the Amenity Mod"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent an amenity.
    
    Attributes:
        name (str): The name of the amenity.

    Methods:
        __init__: Constructor of the Amenity class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Init an Amenity instance"""
        super().__init__(*args, **kwargs)
