#!/usr/bin/python3
"""Testing User class
"""
import unittest
from models.user import User
import models
import os

class TestUser(unittest.TestCase):
    def test_01_email_type(self):
        user = User()
        self.assertEqual(type(user.email), str)
    
    def test_02_password_type(self):
        user = User()
        self.assertEqual(type(user.password), str)

    def test_03_first_name_type(self):
        user = User()
        self.assertEqual(type(user.first_name), str)
    
    def test_04_last_name_type(self):
        user = User()
        self.assertEqual(type(user.last_name), str)

    def test_04_instance_user(self):
        user = User()
        self.assertIsInstance(user, User)
    
    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.engine.file_storage.__doc__
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

if __name__ == "__main__":
    unittest.main()
