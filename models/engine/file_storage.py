"""
Class to storage all the obj
save to a file named 'file.json'
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Name of the file to save
    Dic to save objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the objects in instance
        """
        return self.__objects

    def new(self, obj):
        """
        create a new obj and update dic
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects.update({key: obj})

    def save(self):
        """
        Save the file in a JSON format
        """
        tmp_dic = {}
        for key, value in self.__objects.items():
            tmp_dic[key] = value.to_dict()
        with open(self.__file_path, mode="w") as save_file:
            json.dump(tmp_dic, save_file)

    def reload(self):
        """
        Reload the file anc load de objs
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r") as save_file:
                load = json.load(save_file)
            for value in load.values():
                create = "{}(**value)".format(value["__class__"])
                obj = eval(create)
                self.new(obj)
