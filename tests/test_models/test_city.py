#!/usr/bin/python3
"""Testing city
"""
import unittest
import os
import models
from models.city import City


class TestCity(unittest.TestCase):
    """city testing
    """

    # testing types attributes
    def test_01_name_type(self):
        city = City()
        self.assertEqual(type(city.name), str)

    def test_02_state_id_type(self):
        city = City()
        self.assertEqual(type(city.state_id), str)

    # testing instance of city
    def test_03_instace_city(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.city.__doc__
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
