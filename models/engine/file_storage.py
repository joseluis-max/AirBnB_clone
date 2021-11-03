#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON
"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__+ "." + obj.id] = obj
    
    def save(self):
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(d, file, default=str)
        
    
    def reload(self):
        tmp = {}
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                tmp = json.load(file)
        except (OSError, ValueError):
            pass
        for key, value in tmp.items():
            self.__objects[key] = BaseModel(**value)
    
