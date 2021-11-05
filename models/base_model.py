#!/usr/bin/python3
""" Base Model Implementation """
import uuid
from datetime import datetime
import models



class BaseModel:
    """Defines all common attributes/methods for other classes
    """

    def __init__(self, **kargs):
        """Constructor
            ==========

            Attr:
            ----
                - `id`: (string) random unique id with uuid4
                - `created_at`: (string) created datetime
                - `updated_at`: (string) updated datetime
            
            Args:
            ----
                - `**kargs`: key value arguments
        """
        if kargs and len(kargs) > 0:
            self.id = kargs.get('id')
            self.created_at = datetime.strptime(kargs.get('created_at'), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kargs.get('updated_at'), "%Y-%m-%dT%H:%M:%S.%f")
            # self.name = kargs.get('name')
            # self.my_number = kargs.get('my_number') 
        else:
            self.id = str(uuid.uuid4())
            dt = datetime.now()
            self.created_at = dt
            self.updated_at = dt
            models.storage.new(self)

    def __str__(self):
        """Return a representation in string of the instance

            Return: string representation of instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the created datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation instance

            Return: Dictionary representation of instance
        """
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
