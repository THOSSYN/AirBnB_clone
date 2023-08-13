#!/usr/bin/env python3
"""A program that contains the entry point of
the command line interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Creates a class that handles the cmd console"""
    prompt = "(hbnb) "
    __models = ["BaseModel", "Place", "User",
                "State", "City", "Amenity", "Review"]

    def precmd(self, line):
        """ returns the line to be executed by onecmd """

        for model in self.__models:
            if model in line and "." in line:
                line = line.split(".")
                if "(" in line[1]:

                    if '"' in line[1]:
                        prt = line.pop()
                        prt = prt.split("(")
                        line.append(prt[0])
                        prt2 = prt[1][1:-2]
                        line.append(prt2)

                        return f'{line[1]} {line[0]} {line[2]}'

                    prt = line.pop()
                    prt = prt.split("()")
                    line.append(prt[0])
                    return f'{line[1]} {line[0]}'
                else:
                    return f'{line[1]} {line[0]}'

        return line

    def do_create(self, line):
        """ Creates a new instance of a basemodel and saves it to the
        json file """

        if not line:
            print("** class name missing **")

        elif line in self.__models:
            if line == "BaseModel":
                obj = BaseModel()
                storage.save()
                print(obj.id)

            elif line == "User":
                obj = User()
                storage.save()
                print(obj.id)

            elif line == "State":
                obj = State()
                storage.save()
                print(obj.id)

            elif line == "City":
                obj = City()
                storage.save()
                print(obj.id)

            elif line == "Amenity":
                obj = Amenity()
                storage.save()
                print(obj.id)

            elif line == "Place":
                obj = Place()
                storage.save()
                print(obj.id)

            else:
                obj = Review()
                storage.save()
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

        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) != 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        storage.reload()
        inst_dict = storage.all()
        to_show = f'{args[0]}.{args[1]}'

        if to_show in inst_dict:
            print(inst_dict[to_show])
            return

        print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes the instance of a base model in the storage and
        updates the value in the json file."""
        args = args.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) != 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        storage.reload()
        inst_dict = storage.all()
        to_del = ""

        for key, value in inst_dict.items():
            if obj_id == value.id:
                to_del = key

        if to_del != "":
            del inst_dict[to_del]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """ Prints are the BaseModel instances in the storage
        as a list."""

        args = args.split()

        if args and args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        rep_list = []
        if args:
            storage.reload()
            inst_dict = storage.all()
            for key, value in inst_dict.items():
                if args[0] in key:
                    rep_list.append(str(value))
        else:
            storage.reload()
            inst_dict = storage.all()
            for key, value in inst_dict.items():
                rep_list.append(str(value))

        print(rep_list)

    def do_count(self, args):
        """ Counts the number of instances. """

        args = args.split()
        count = 0

        if args and args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        if args:
            storage.reload()
            inst_dict = storage.all()
            for key, value in inst_dict.items():
                if args[0] in key:
                    count += 1
        else:
            storage.reload()
            inst_dict = storage.all()
            for key, value in inst_dict.items():
                count += 1

        print(count)

    def do_update(self, args):
        """ Updates the attributes of an instance in the json file."""
        args = args.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.__models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        # confirm if the id exists
        obj_id = args[1]
        storage.reload()
        inst_dict = storage.all()
        id_check = ""

        for key, value in inst_dict.items():
            if obj_id == value.id:

                # id_check will hold the key to the
                # basemodel object with the given id, if it exists
                id_check = key

        if id_check == "":
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        # retrieve the value of the key from the id_check
        # implement the update
        bm_obj = inst_dict[id_check]

        if args[2] in bm_obj.to_dict():
            bm_obj.__dict__[args[2]] = str(args[3])
        else:
            bm_obj.__dict__[args[2]] = str(args[3])

        bm_obj.save()

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

    # def postloop(self):
    #     """ Command to execute after the loop is exited. """
    #     print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
