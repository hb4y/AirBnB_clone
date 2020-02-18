import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the HBNB console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit the console"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """exit on EOF"""
        return True

    def help_EOF(self):
        print("EOF command to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
