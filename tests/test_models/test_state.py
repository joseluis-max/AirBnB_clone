#!/usr/bin/python3
"""Testing State
"""
import unittest
import os
import models
from models.state import State


class TestState(unittest.TestCase):
    """State testing
    """

    # testing types attributes
    def test_01_name_type(self):
        state = State()
        self.assertEqual(type(state.name), str)
    
    # testing instance of state
    def test_02_instace_state(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_docstring(self):
        """ function test_docstring """
        msj = "Module doesnt have docstring"
        obj = models.state.__doc__
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
