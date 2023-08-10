#!/usr/bin/env python3
"""A program that contains the entry point of
the command line interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

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
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ The show method displays the string representation of
        a basemodel based on class name and id """

        # Argument in args is a tuple, taking all argument
        # as a string, this is why you have to split it
        # by the delimiter used to enter the arguments
        args = args.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) != 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        storage.reload()
        inst_dict = storage.all()

        for key, value in inst_dict.items():
            if obj_id == value.id:
                print(value)
                return

        print("** no instance found **")

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
