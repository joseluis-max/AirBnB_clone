#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON
"""
import json
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON

        Attr:
            file_path: (str) file path where save the data
            objects: (dict) Collection of instance of class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrun Objects class attribute
        """
        return self.__objects

    def new(self, obj):
        """Add a new instance of obj to __objects
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Save in json the objects dictionary like a dictionary of dictionary
            representation instances of BaseModel
        """
        dictionary = {}
        for key, value in self.__objects.items():
            dictionary[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(dictionary, file, default=str, sort_keys=True, indent=4)

    def reload(self):
        """Reload data from json to __objects like instances of BaseModel
        """
        try:
            stream = {}
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                stream = json.load(file)
            for key, value in stream.items():
                self.__objects[key] = eval(value.get("__class__"))(**value)
        except (OSError, ValueError):
            pass
