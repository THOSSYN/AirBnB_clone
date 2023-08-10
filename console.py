#!/usr/bin/env python3
"""A program that contains the entry point of
the command line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Creates a class that handles the cmd console"""
    prompt = "(hbnb) "

    def do_quit(self, command):
        """Functionality for quitting the console"""
        return True

    def do_EOF(self, command):
        """Exit gracefully when end of file is signaled """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
