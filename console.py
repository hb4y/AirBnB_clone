#!/usr/bin/python3

import cmd


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
        exit on EOF
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
