# This the Airbnb Clone project
Decription: As of the day, airbnb is one of the world leading reservation
service providers. In the project, we are building a clone of the website.
We do not intend to replicate all its features, this only covers some basic
concept of the actual website itself.
The project is in phase and this is the console development stage to manipulate
the date without a GUI.
The Airbnb clone is our first full web application.

How to use the Console
=======================
The console is a command interpreter, meaning it takes in some text or argument
and the argument is 'parsed' to execute the expected implementation.
The interpreter works both in interactive and non-interactive modes.
You can also directly pass argument to the console.

## Demonstrations
____________________
`$ ./console.py # interactive mode`\n
(hbnb)
(hbnb) help
(hbnb) help

` Documented commands (type help <topic>):`
 `=========================================`
` EOF  help  quit `

 (hbnb)
 (hbnb)
 (hbnb) quit
 $
 `$ echo "help" | ./console.py	# non-interactive mode, passing arguments`
 (hbnb)

` Documented commands (type help <topic>):`
`========================================`
 `EOF  help  quit`
 `(hbnb)`
 $
 $ cat test_help
 $ cat test_help | ./console.py     # non-interactive mode, reading from a file
 (hbnb)

 `Documented commands (type help \<topic\>):`
`========================================`
 `EOF  help  quit`
 `(hbnb)`
 `$`