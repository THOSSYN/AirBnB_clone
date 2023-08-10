#!/usr/bin/env python3
"""A program that contains the entry point of
the command line interpreter"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Creates a class that handles the cmd console"""
    prompt = "(hbnb) "

    def do_create(self, line):
        """ Creates a new instance of a basemodel and saves it to the
        json file """

        if not line:
            print("** class name missing **")
        elif line == "BaseModel":
            obj = BaseModel()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def emptyline(self):
        """ The emptyline method called when an empty line
        is entered """
        return ""

    def do_quit(self, command):
        """Functionality for quitting the console"""
        return True

    def do_EOF(self, command):
        """Exit gracefully when end of file is signaled """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
