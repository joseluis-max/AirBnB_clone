#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    #testing types data
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
        self.assertEqual(type(base.create_at), str)
    
    def test_05_update_at_type(self):
        base = BaseModel()
        self.assertEqual(type(base.update_at), str)
    
    
if __name__ == "__main__":
    unittest.main()
