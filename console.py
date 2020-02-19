#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import classes, storage


class HBNBCommand(cmd.Cmd):
    """Class for the HBNB console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit the console
        """
        return True

    def do_EOF(self, arg):
        """
        Exit on EOF
        """
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldnt execute anything
        """
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg and not (arg in classes):
            print("** class name doesn't exist **")
        else:
            create = "{}()".format(arg)
            obj = eval(create)
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        if not arg:
            print("** class name is missing **")
        elif not (arg.split()[0] in classes):
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            dic_all = storage.all()
            name = str(arg.split()[0]) + "." + str(arg.split()[1])
            for key in dic_all.keys():
                if key == name:
                    print(dic_all[key])
                    return False
            print("** no instance found **")

    def do_destroy(self, arg):
        if not arg:
            print("** class name is missing **")
        elif not (arg.split()[0] in classes):
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        else:
            dic_all = storage.all()
            name = str(arg.split()[0]) + "." + str(arg.split()[1])
            for key in dic_all.keys():
                if key == name:
                    dic_all.pop(key)
                    storage.save()
                    return False
            print("** no instance found **")

    def do_update(self, arg):
        if not arg:
            print("** class name is missing **")
        elif not (arg.split()[0] in classes):
            print("** class doesn't exist **")
        elif len(arg.split()) < 2:
            print("** instance id missing **")
        elif len(arg.split()) < 3:
            print("** attribute name missing **")
        elif len(arg.split()) < 4:
            print("** value missing **")
        else:
            dic_all = storage.all()
            name = str(arg.split()[0]) + "." + str(arg.split()[1])
            for key in dic_all.keys():
                if key == name:
                    setattr(dic_all[name], arg.split()[2], arg.split()[3])
                    storage.save()
                    return False
            print("** no instance found **")

    def do_all(self, arg):
        if not arg:
            dic_all = storage.all()
            for key in dic_all.keys():
                if key.startswith(arg):
                    print(dic_all[key])
            return False
        elif not (arg in classes):
            print("** class does't exist **")
        else:
            dic_all = storage.all()
            for key in dic_all.keys():
                if key.startswith(arg):
                    print(dic_all[key])
            return False 

if __name__ == '__main__':
    HBNBCommand().cmdloop()
