#!/usr/bin/python3

"""define place Module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represent place class

    Attributes:
        city_id (str): id of City
        user_id (str): is of User
        name (str): name of place
        description (str): description of place
        number_rooms (int): Number of rooms
        number_bathrooms (int): Number of bathrooms
        max_guest (int): Maximum number of guests
        price_by_night (int): Price by night
        latitude (float): Latitude
        longitude (float): Longitude
        amenity_ids (list): List of Amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes a Place instance"""
        super().__init__(*args, **kwargs)
