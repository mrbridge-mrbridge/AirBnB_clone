### 0x00. AirBnB clone - The console

<img src="https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67" alt="Hbnb">

### Authors
<h3> <a href="mailto:lesliedeeshumba@gmail.com">Leslie Danai Shumba</a> </h3>
<h3> <a href="mailto:nanamcroj@gmail.com">Richard Osei Juantuah</a> </h3>

### First step: Write a command interpreter to manage your AirBnB objects
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances

* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

* create the first abstracted storage engine of the project: File storage.

* create all unittests to validate all our classes and storage engine

### Execution
Should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Works like this in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

<h2>Project Flow</h2>

<img src="https://i.imgur.com/ovMNyEZ.png" alt="flow chart" >
