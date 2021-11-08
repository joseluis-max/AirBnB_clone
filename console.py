#!/usr/bin/python3
"""Console
"""
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ My first in Python"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit from prompt"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        return False

    def do_create(self, line):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if (line == ""):
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "State",
                          "Review", "Place", "City", "Amenity"]:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an
            instance based on the class name and id.
        """
        line = line.split(" ")
        if (line[0] == ""):
            print("** class name missing **")
        elif line[0] not in ["BaseModel", "User", "State", "Review",
                             "Place", "City", "Amenity"]:
            print("** class doesn't exist **")
        elif (len(line) == 1):
            print("** instance id missing **")
        else:
            try:
                with open("file.json", mode="r", encoding="utf-8") as file:
                    tmp = json.load(file)
                    for key, value in tmp.items():
                        split = key.split(".")
                        if (line[0] == split[0] and line[1] == split[1]):
                            base = eval(tmp[key]['__class__'])(**value)
                            print(base.__str__())
                            return
            except FileNotFoundError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and
            id (save the change into the JSON file).
        """
        line = line.split(" ")

        if (line[0] == ""):
            print("** class name missing **")
        elif line[0] not in ["BaseModel", "User", "State", "Review",
                             "Place", "City", "Amenity"]:
            print("** class doesn't exist **")
        elif (len(line) == 1):
            print("** instance id missing **")
        else:
            with open("file.json", mode="r", encoding="utf-8") as file:
                stream = json.load(file)
                try:
                    stream.pop(line[0] + "."+line[1])
                    with open("file.json", mode="w",
                                encoding="utf-8") as file:
                        json.dump(stream, file, sort_keys=True, indent=4)
                    return
                except (KeyError, AttributeError, OSError):
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all
            instances based or not on the class name.
            Ex: $ all BaseModel or $ all
        """
        if line in ["BaseModel", "User", "State", "Review",
                    "Place", "City", "Amenity", ""]:
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
        elif line[0] not in ["BaseModel", "User", "State", "Review",
                             "Place", "City", "Amenity"]:
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
                        json.dump(stream, file, sort_keys=True, indent=4)
            except (OSError, KeyError):
                print("** no instance found **")

    def do_count(self, line):
        """Count the string representation of
            an instance based on the class name.
        """
        i = 0
        if (line == ""):
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "State", "Review",
                          "Place", "City", "Amenity"]:
            print("** class doesn't exist **")
        else:
            with open("file.json", mode="r", encoding="utf-8") as file:
                tmp = json.load(file)
                for key in tmp:
                    split = key.split(".")
                    if (line == split[0]):
                        i += 1
                print(i)

    def default(self, line):
        try:
            split_line = line.split(".")
            command = split_line[1].split("(")
            if (command[0] == "all"):
                self.do_all(split_line[0])
            elif (command[0] == "count"):
                self.do_count(split_line[0])
            elif (command[0] == "show"):
                id = command[1][1:-2]
                new_line = split_line[0] + " " + id
                self.do_show(new_line)
            elif (command[0] == "destroy"):
                id = command[1][1:-2]
                new_line = split_line[0] + " " + id
                print(new_line)
                self.do_destroy(new_line)
            elif (command[0] == "update"):
                data = command[1].split(",")
                id = data[0][1:-1]
                attr = data[1][2:-1]
                value = data[2][2:-2]
                new_line = split_line[0] + " " + id + " " + attr + " " + value
                self.do_update(new_line)
        except (AttributeError, KeyError, IndexError):
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
