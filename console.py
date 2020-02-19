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
        """
        Create a new obj
        """
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
        """
        Show a specific class + instance id
        """
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
        """
        Destroy an obj with a specific class + instance id
        """
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
                    del(dic_all[key])
                    storage.save()
                    return False
            print("** no instance found **")

    def do_update(self, arg):
        """
        Update the obj with: class_name + id + attrib + value
        """
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
                    if arg.split()[3].isdecimal():
                        aux_val = int(arg.split()[3])
                    else:
                        try:
                            aux_val = float(arg.split()[3])
                        except ValueError:
                            aux_val = arg.split()[3]

                    setattr(dic_all[name], arg.split()[2], aux_val)
                    storage.save()
                    return False
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print all obj OR print objs with specific class_name
        """
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
