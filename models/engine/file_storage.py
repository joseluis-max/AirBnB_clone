#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON
    
        Attr:
            file_path: (str) file path where save the data
            objects: (dict) Collection of instance of BaseModel class
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Retrun Objects class attribute
        """
        return self.__objects

    def new(self, obj):
        """Add a new instance of BaseModel to __objects
        """
        self.__objects[obj.__class__.__name__+ "." + obj.id] = obj
    
    def save(self):
        """Save in json the objects dictionary like a dictionary of dictionary
            representation instances of BaseModel
        """
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(d, file, default=str)
        
    def reload(self):
        """Reload data from json to __objects like instances of BaseModel
        """
        tmp = {}
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                tmp = json.load(file)
        except (OSError, ValueError):
            pass
        for key, value in tmp.items():
            self.__objects[key] = eval(value.get("__class__"))(**value)
    