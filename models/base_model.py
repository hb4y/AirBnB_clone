""" base_model The mold(idea) class is the parent class."""
import uuid
from datetime import datetime


class BaseModel:
    """class initialization"""
    def __init__(self, *args, **kwargs):
        """ initialization"""
        if kwargs:
            

        else:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """should print, and str() should return"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())

    def save(self):
        """comentario"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to new dict"""
        to_new_dict = self.__dict__
        to_new_dict["__class__"] = self.__class__.__name__
        to_new_dict["created_at"] = self.created_at.isoformat()
        to_new_dict["updated_at"] = self.updated_at.isoformat()
        return to_new_dict
    
