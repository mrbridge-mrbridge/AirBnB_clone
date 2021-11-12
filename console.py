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


def HBNBCommand(cmd.Cmd):
    """Hbnb Shell"""
    intro = 'Welcome to the Hbnb shell"
    prompt = '(hbnb)'

    def emptyline(self):
        """Empty-line"""
        pass

        inslist = {'BaseModel': Basemodel, 'City': City, 'State': State,
               'Place': Place, 'User': User, 'Amenity': Amenity,
               'Review': Review}

    def do_create(self, inlist = None):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not inlist:
            print('** class name missing **')
        elif not self.inlist.get(inlist):
            print('** class doesn\'t exist **')


    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        inslist = None
        opk = None
        args = arg.split(' ')
        if len(args) > 0:
            inslist = args[0]
        if len(args) > 1:
            opk = args[1]
        if not inslist:
            print('** class name missing **')
        elif not self.inlist.get(inlist):
            print ('** class doesn\'t exist **')
        elif not opk:
            print('** instance id missing **')
        else:
            t = inslist + "."opk
            object = models.storage.all().get(t)
            if not object:
                print('** no instance found **')
            else:
                print(object)


    def do_destroy()
    def do_all()
    def do_update()

    def do_quit(self, arg):
        """ Quit Command"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the console"""
        return True


if __name__ == '__main__':
    HBNBCommand()cmd.loop()
