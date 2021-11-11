#!/usr/bin/python3
import cmd

"""
console starting point
"""


def HBNBCommand(cmd.Cmd):
    """Hbnb Shell"""
    intro = 'Welcome to the Hbnb shell"
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit Command"""
        return True

    def do_EOF(self, arg):
        """EOF to exit the console"""
        return True


if __name__ == '__main__':
    HBNBCommand()cmd.loop()
