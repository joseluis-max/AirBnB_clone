#!/usr/bin/python3
"""Testing BaseModel case
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
import models
import os

class TestBase(unittest.TestCase):
    # testing types data
    def test_01_str_type(self):
        base = BaseModel()
        string = base.__str__()
        self.assertEqual(type(string), str)
    
    def test_02_to_dict_type(self):
        base = BaseModel()
        dictionary = base.to_dict()
        self.assertEqual(type(dictionary), dict)

    def test_03_id_type(self):
        base = BaseModel()
        self.assertEqual(type(base.id), str)
    
    def test_04_create_at_type(self):
        base = BaseModel()
        self.assertEqual(type(base.created_at), datetime)
    
    def test_05_update_at_type(self):
        base = BaseModel()
        self.assertEqual(type(base.updated_at), datetime)
    
    def test_06_date_to_string(self):
        base = BaseModel().to_dict()
        self.assertEqual(type(base['created_at']), str)
        self.assertEqual(type(base['updated_at']), str)

    def test_07_update_at_type_after_update(self):
        base = BaseModel()
        base.save()
        self.assertEqual(type(base.updated_at), datetime)

    # test not equal id
    def test_08_not_equal_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    # test update before save
    def test_09_update_before_save(self):
        base = BaseModel()
        u1 = base.updated_at
        base.save()
        u2 = base.updated_at
        self.assertNotEqual(u1, u2)

    # test create_at and update_at are equal when create a intance
    def test_10_create_at_equal_to_update_at_new_instance(self):
        base = BaseModel()
        self.assertEqual(base.created_at, base.updated_at)

    # test save method
    def test_11_save_method(self):
        base = BaseModel()
        base.save()
        with open("file.json", mode="r", encoding="utf-8") as file:
            self.assertIn(base.id, file.read())

    # test diccionary update automatically update_at
    def test_12_diccionary_automatically_update_at(self):
        base = BaseModel()
        d1 = base.to_dict()
        base.save()
        d2 = base.to_dict()
        self.assertNotEqual(d1["updated_at"], d2["updated_at"])

    # test str format
    def test_13_str_format(self):
        s = "[BaseModel] ({}) {}"
        base = BaseModel()
        self.assertEqual(base.__str__(), s.format(base.id, base.__dict__))

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.base_model.__doc__
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
