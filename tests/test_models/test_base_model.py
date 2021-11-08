#!/usr/bin/python3
"""Testing BaseModel case
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
import models
import os
import inspect
from unittest import mock
module_doc = models.base_model.__doc__


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
        self.assertNotEqual(base.created_at, base.updated_at)

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

    # test attributes
    def test_14_attrs(self):
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    # test __class__ to dict
    def test_15_class_(self):
        base = BaseModel()
        d = base.to_dict()
        self.assertTrue(hasattr(base.__dict__, "__class__"))

    def test_uuid(self):
        """Test that id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

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
