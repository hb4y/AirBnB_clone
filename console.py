#!/usr/bin/python3

import cmd
from models.base_model import BaseModel


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
