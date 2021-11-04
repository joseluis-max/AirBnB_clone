#!/usr/bin/python3
"""Console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ My first in Python"""

    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Exit from prompt"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True
    
    def do_emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
