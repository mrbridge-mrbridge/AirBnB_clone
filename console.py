#!/usr/bin/python3
"""This module is the entry point of the Airbnb command interpreter"""
import cmd, sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Nothing"""
        return False

    def do_create(self, arg, __name__):
        """Create command to create and save new BaseModel
        instance to JSON file and print the id"""

        if __name__ is None:
            return "** class name missing **"

        if __name__ not in classes[keys].items():
            return "** class doesn't exist **"
        new = BaseModel()
        BaseModel.save(new)
        return new.id

    def do_show(self, arg, __name__, id):
        """Show command prints the string representation of class instance"""
        if __name__ is None:
            return "** class name missing **"

        if __name__ not in classes[keys].items():
            return "** class doesn't exist **"

        if id is None:
            return "** instance id missing **"

        if id != __name__.id:
            return "** no instance found **"

        return "[{}] ({}) {}".format(__name__, __name__.id, __name__.__dict__)

    def do_destroy(self, arg, __name__, id):
        """Destroy command deletes a class instance based on 
        class name and id"""
        if __name__ is None:
            return "** class name missing **"

        if __name__ not in classes[keys].items():
            return "** class doesn't exist **"

        if id is None:
            return "** instance id missing **"

        if id != __name__.id:
            return "** no instance found **"
        dikt = BaseModel.to_dict()
        if __name__ in dikt:
            del __name__
        BaseModel.save()
        return

    def do_all(self, arg, **args):
        """All command Prints all string representation of all
        instances based or not on the class name"""
        if len(args) == 0:
            BaseModel.__str__()
            return
        for i in args:
            if i not in classes:
                return "** class doesn't exist **"
        BaseModel.__str__()
        return

    def do_update(self, arg, __name__, id, **args):
        """Update command Updates an instance based on the class
        name and id by adding or updating attribute

        Usage: update <class name> <id> <attribute name> '<attribute value>'
        """
        if len(args) >= 2:
            for k, v in kwargs.items():
                k = args[0]
                v = args[1]
            BaseModel(__name__, id, **kwargs)

        if __name__ is None:
            return "** class name missing **"

        if __name__ not in classes[keys].items():
            return "** class doesn't exist **"

        if id is None:
            return "** instance id missing **"

        if id != __name__.id:
            return "** no instance found **"

        if len(args) == 0:
            return "** attribute name missing **"

        if len(args) == 1:
            return "** value missing **"
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
