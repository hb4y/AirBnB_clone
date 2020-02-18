import json
import os
from models.base_model import BaseModel



class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects.update({key: obj})

    def save(self):
        tmp_dic = {}
        with open(self.__file_path, mode="w") as save_file:
            for key, value in self.__objects.items():
                tmp_dic[key] = value.to_dict()
            json.dump(tmp_dic, save_file)

    def reload(self):
        if os.path.exists(self.__file_path): 
            with open(self.__file_path, mode="r") as save_file:
                load = json.load(save_file)
            for value in load.values():
                create = "{}(**value)".format(value["__class__"])
                obj = eval(create)
                self.new(obj)
