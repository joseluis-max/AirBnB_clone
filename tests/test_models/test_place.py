#!/usr/bin/python3
"""Testing place
"""
import unittest
import os
import models
from models.place import Place


class TestAmenity(unittest.TestCase):
    """Amenity testing
    """

    # testing types attributes
    def test_01_city_id_type(self):
        place = Place()
        self.assertEqual(type(place.city_id), str)

    def test_02_user_id_type(self):
        place = Place()
        self.assertEqual(type(place.user_id), str)

    def test_03_name_type(self):
        place = Place()
        self.assertEqual(type(place.name), str)

    def test_05_description_type(self):
        place = Place()
        self.assertEqual(type(place.description), str)

    def test_06_numbers_rooms_type(self):
        place = Place()
        self.assertEqual(type(place.number_rooms), int)
    
    def test_07_number_bathrooms_type(self):
        place = Place()
        self.assertEqual(type(place.number_bathrooms), int)

    def test_08_max_guest_type(self):
        place = Place()
        self.assertEqual(type(place.max_guest), int)

    def test_09_pryce_by_night_type(self):
        place = Place()
        self.assertEqual(type(place.price_by_night), int)

    def test_10_latitude_type(self):
        place = Place()
        self.assertEqual(type(place.latitude), float)
    
    def test_11_longitude_type(self):
        place = Place()
        self.assertEqual(type(place.longitude), float)
    
    def test_12_amenity_ids_type(self):
        place = Place()
        self.assertEqual(type(place.amenity_ids), list)

    # testing instance of place
    def test_13_instace_amenity(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.place.__doc__
        self.assertIsNotNone(obj, msj)
        msj = "Classes doesnt have docstring"
        self.assertIsNotNone(obj, msj)

    def test_executable_file(self):
        """ function test_executable_file """
        is_read_true = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(is_write_true)
        is_exec_true = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(is_exec_true)
