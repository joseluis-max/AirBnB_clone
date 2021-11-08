# AirBnB_clone Console

Interpreter to manage my AirBnB_clone objects.

Console, is the first step towards building my first full web application: the AirBnB clone. This console is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

**We want to be able to manage the objects of our project:**

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### How to start it ?

1. Clone this repository.
2. Execute console.py file
    ```
    $ ./console.py
    ```
3. Introduce one command to next list.
### How to used it ?
- `create <class_name>`: create a new instance.
- `show <class_name> <id>` or `<class_name>.shoe(<id>)`: show the instance.
- `destroy <class_name> <id>` or `<class_name>.destroy(<id>)`: delete a instance
- `all`: print all instances
- `all <class_name>` or `<class_name>.all()`: print all class_name instances
- `update <class_name> <id> <attribute_name> <new_value>` or `<class_name>.update(<id>, <attribute_name>, <value>)`: update an attribute of class_name.id
- `count <class_name` or `<class_name>.count()`: counter class_name instances
