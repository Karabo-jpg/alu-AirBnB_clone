#!/usr/bin/python3
"""
Command Interpreter Module for HBNB Project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF to exit the program (Ctrl+D)"""
        print()  # Print newline for clean exit
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
