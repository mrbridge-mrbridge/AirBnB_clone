### 0x00. AirBnB clone - The console

<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20211109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211109T205320Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=452096f1f04e678de9ba62eb6806f518b4041c8f004a3febcda4907080cea8b8" alt="Hbnb"/>

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

<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20211109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211109T205320Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5bdf2f8f7c725065ecd0680253d9c700f069950abbf6a4ff6fb667deb8176305" alt="flow chart" />
