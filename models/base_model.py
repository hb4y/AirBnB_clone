""" base_model The mold(idea) class is the parent class."""
import uuid
from datetime import datetime, date
import models
"""
Base_model The mold(idea).
Is the parent class.
"""


class BaseModel:
    """
    class initialization
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key == "updated_at":
                        self.updated_at = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key == "id":
                        self.id = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Should print, and str() should return
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.to_dict()))

    def save(self):
        """update 'updated_at' attribute"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ to new dict"""
        to_new_dict = self.__dict__.copy()
        to_new_dict["__class__"] = self.__class__.__name__
        to_new_dict["created_at"] = to_new_dict["created_at"].isoformat()
        to_new_dict["updated_at"] = to_new_dict["updated_at"].isoformat()
        return to_new_dict
