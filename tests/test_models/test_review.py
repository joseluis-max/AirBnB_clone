#!/usr/bin/python3
"""Testing review
"""
import unittest
import os
import models
from models.review import Review


class TestReview(unittest.TestCase):
    """Review testing
    """

    # testing types attributes
    def test_01_place_id_type(self):
        review = Review()
        self.assertEqual(type(review.place_id), str)
    
    def test_02_user_id_type(self):
        review = Review()
        self.assertEqual(type(review.user_id), str)
    
    def test_03_text_type(self):
        review = Review()
        self.assertEqual(type(review.text), str)

    # testing instance of review
    def test_04_instace_amenity(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.review.__doc__
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
