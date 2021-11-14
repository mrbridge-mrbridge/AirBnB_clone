#!/usr/bin/python3
import cmd
import models
from models.base_model import Basemodel
from models.City import City
from models.State import State
from models.Place import Place
from models.User import User
from models.Amenity import Amenity
from models.Review import Review

"""
console starting point
"""


class HBNBCommand(cmd.Cmd):
    """Hbnb Shell"""
    prompt = '(hbnb)'

    def emptyline(self):
        """Empty-line"""
        pass

        inslist = {'BaseModel': Basemodel, 'City': City, 'State': State,
                   'Place': Place, 'User': User, 'Amenity': Amenity,
                   'Review': Review}

    def do_create(self, inlist=None):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not inlist:
            print('** class name missing **')
        elif not self.inlist.get(inlist):
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        inslist = None
        opk = None
        args = arg.split(' ')
        if len(args) > 0:
            inslist = args[0]
        if len(args) > 1:
            opk = args[1]
        if not inslist:
            print('** class name missing **')
        elif not self.inslist.get(inslist):
            print('** class doesn\'t exist **')
        elif not opk:
            print('** instance id missing **')
        else:
            t = inslist + "." + opk
            object = models.storage.all().get(t)
            if not object:
                print('** no instance found **')
            else:
                print(object)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name"""
        inslist = None
        opk = None
        args = arg.split(' ')
        if len(args) > 0:
            inslist = args[0]
        if len(args) > 1:
            opk = args[1]
        if not inslist:
            print('** class name missing **')
        elif not self.inslist.get(inslist):
            print('** class doesn\'t exist **')
        elif not opk:
            print('** instance id missing **')
        else:
            t = inslist + "." + opk
            object = models.storage.all().get(t)
            if not object:
                print('** no instance found **')
            else:
                del models.storage.all()[t]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
         based or not on the class name"""
        if not arg:
            print([str(value) for key, value in models.storage.all().items()])
        else:
            if not self.inlist.get(arg):
                print('** class doesn\'t exist **')
                return False
            print([str(value) for key, value in models.storage.all()
                   .items()
                   if type(value) is self.inlist.get(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class nameUpdates an
         instance based on the class name"""
        from datetime import datetime
        from shlex import shlex

        updatetime = datetime.now()
        args = arg.split(' ', 3)
        inslist = None
        opk = None
        aval = None
        attr = None
        if len(args) > 0:
            inslist = args[0]
        if len(args) > 1:
            opk = args[1]
        if len(args) > 3:
            aval = list(shlex(args[3]))[0].strip('"')
        if len(args) > 2:
            attr = args[2]
        if not inslist:
            print('** class name missing **')

        elif not self.inslist.get(inslist):
            print('** class doesn\'t exist **')

        elif not opk:
            print('** instance id missing **')

        else:
            t = inslist + "." + opk
            object = models.storage.all().get(t)
            if not object:
                print('** no instance found **')
            else:
                if hasattr(object, attr):
                    aval = type(getattr(object, attr))(aval)
                else:
                    aval = type(getattr(object, attr))(aval)
                    setattr(object, attr, aval)
                    object.updated_at = updatetime
                    models.storage.save()

    def do_quit(self, arg):
        """ Quit Command"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the console"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
