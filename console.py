#!/usr/bin/python3
"""Console
"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User


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
    
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if (line == ""):
            print("** class name missing **")
        elif line not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)
        
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id.
        """
        line = line.split(" ")
        if (line[0] == ""):
            print("** class name missing **")
        elif line[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif (len(line) == 1):
            print("** instance id missing **")
        else:
            with open("file.json", mode="r", encoding="utf-8") as file:
                tmp = json.load(file)
                for key, value in tmp.items():
                    split = key.split(".")
                    if (line[1] == split[1]):
                        base = eval(tmp[key]['__class__'])(**value)
                        print(base.__str__())
                        return;
            print("** no instance found **")
        
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file). 
        """
        line = line.split(" ")
        
        if (line[0] == ""):
            print("** class name missing **")
        elif line[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif (len(line) == 1):
            print("** instance id missing **")
        else:
            with open("file.json", mode="r", encoding="utf-8") as file:
                tmp = json.load(file)
                try:
                    if (tmp[line[0] + "."+line[1]] != None):
                        
                        with open("file.json", mode="w", encoding="utf-8") as file:
                            json.dump(tmp, file)
                        return
                except:
                    print("** no instance found **")
    
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name. 
            Ex: $ all BaseModel or $ all
        """
        if line in ["BaseModel", "User", ""]:
            instances = []
            with open("file.json", mode="r", encoding="utf-8") as file:
                stream = json.load(file)
                if (line != ""):
                    for key, value in stream.items():
                        if (stream[key]['__class__'] == line):
                            base = eval(stream[key]['__class__'])(**value)
                            instances.append(base.__str__())
                else:
                    for key, value in stream.items():
                            base = eval(stream[key]['__class__'])(**value)
                            instances.append(base.__str__())
                print(instances)
        else:
            print("** class doesn't exist **")
        
    def do_update(self, line):
        """Updates an instance based on the class name and id by 
            adding or updating attribute (save the change into the JSON file).
        """
        line = line.split(" ")
        if (line[0] == ""):
            print("** class name missing **")
        elif line[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        elif (len(line) == 1):
            print("** instance id missing **")
        elif (len(line) == 2):
            print("** attribute name missing **")
        elif (len(line) == 3):
            print("** value missing **")
        else:
            try:
                with open("file.json", mode="r", encoding="utf-8") as file:
                    stream = json.load(file)
                    stream[line[0]+"."+line[1]][line[2]] = line[3]
                    with open("file.json", mode="w", encoding="utf-8") as file:
                        json.dump(stream, file)
            except:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()