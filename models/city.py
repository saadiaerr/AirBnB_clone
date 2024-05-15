#!/usr/bin/python3

""" deine the City Mod"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    represent City class

    Attributes:
        state_id (str): State id
        name (str): name of city

    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Init a City instance"""
        super().__init__(*args, **kwargs)
