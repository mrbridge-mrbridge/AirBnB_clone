#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review

"""
console starting point
"""


class HBNBCommand(cmd.Cmd):
    """Hbnb Shell"""
    prompt = '(hbnb)'

    def emptyline(self):
        """Empty-line"""
        pass

    inslist = {'BaseModel': BaseModel, 'City': City, 'State': State,
               'Place': Place, 'User': User, 'Amenity': Amenity,
               'Review': Review}

    def do_create(self, inslist=None):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not inslist:
            print('** class name missing **')
        elif not self.inslist.get(inslist):
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
            if not self.inslist.get(arg):
                print('** class doesn\'t exist **')
                return False
            print([str(value) for key, value in models.storage.all()
                   .items()
                   if type(value) is self.inslist.get(arg)])

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

    def default(self, line):
        """handle class commands"""
        lva = line.split('.', 1)
        if len(lva) < 2:
            print('*** Unknown syntax:', lva[0])
            return False
        inslist, line = lva[0], lva[1]
        if inslist not in list(self.clslist.keys()):
            print('*** Unknown syntax: {}.{}'.format(inslist, line))
            return False
        lva = line.split('(', 1)
        if len(lva) < 2:
            print('*** Unknown syntax: {}.{}'.format(inslist, lva[0]))
            return False
        mthname, args = lva[0], lva[1].rstrip(')')
        if mthname not in ['all', 'count', 'show', 'destroy', 'update']:
            print('*** Unknown syntax: {}.{}'.format(inslist, line))
            return False
        if mthname == 'all':
            self.do_all(inslist)
        elif mthname == 'count':
            print(self.count_class(inslist))
        elif mthname == 'show':
            self.do_show(inslist + " " + args.strip('"'))
        elif mthname == 'destroy':
            self.do_destroy(inslist + " " + args.strip('"'))
        elif mthname == 'update':
            lb, rb = args.find('{'), args.find('}')
            d = None
            if args[lb:rb + 1] != '':
                d = eval(args[lb:rb + 1])
            lva = args.split(',', 1)
            objid, args = lva[0].strip('"'), lva[1]
            if d and type(d) is dict:
                self.handle_dict(inslist, objid, d)
            else:
                from shlex import shlex
                args = args.replace(',', ' ', 1)
                lva = list(shlex(args))
                lva[0] = lva[0].strip('"')
                self.do_update(" ".join([inslist, objid, lva[0], lva[1]]))

    def handle_dict(self, inslist, objid, d):
        """handle dictionary update"""
        for key, value in d.items():
            self.do_update(" ".join([inslist, objid, str(key), str(value)]))

    def postloop(self):
        """print new line after each loop"""
        print()

    @staticmethod
    def count_class(inslist):
        """count number of objects of type inslist"""
        c = 0
        for key, value in models.storage.all().items():
            if type(value).__name__ == inslist:
                c += 1
        return (c)

    @staticmethod
    def getType(aval):
        """return the type of the input string"""
        try:
            int(aval)
            return (int)
        except ValueError:
            pass
        try:
            float(aval)
            return (float)
        except ValueError:
            return (str)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
