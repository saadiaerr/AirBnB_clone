#!/usr/bin/python3

""" define the Amenity Mod"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represent an amenity.
<<<<<<< HEAD
=======

>>>>>>> 3a286b9e7ed6d43cf49fabf52e39dbd0bc736044
    Attributes:
        name (str): The name of the amenity.

    Methods:
        __init__: Constructor of the Amenity class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Init an Amenity instance"""
        super().__init__(*args, **kwargs)
