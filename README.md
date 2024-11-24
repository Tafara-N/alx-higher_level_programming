# Introduction to programming in `Python`, `JavaScript` and `SQL`.

## Table of Content
- [Author](#author)
- [Description](#description)
___

- [Almost A Circle](0x0C-python-almost_a_circle/README.md)
- [Classes: I](0x06-python-classes/README.md)
- [Classes: II](0x08-python-more_classes/README.md)
- [Data Structures: I](0x03-python-data_structures/README.md)
- [Data Structures: II](0x04-python-more_data_structures/README.md)
- [Everything Is Object](0x09-python-everything_is_object/README.md)
- [Exceptions](0x05-python-exceptions/README.md)
- [Hello World](0x00-python-hello_world/README.md)
- [If, Else, Loops and Functions](0x01-python-if_else_loops_functions/README.md)
- [Import Modules](0x02-python-import_modules/README.md)
- [Inheritance](0x0A-python-inheritance/README.md)
- [Input and Output](0x0B-python-input_output/README.md)
- [Network: I](0x10-python-network_0/README.md)
- [Network: II](0x11-python-network_1/README.md)
- [Object Relational Mapping](0x0F-python-object_relational_mapping/README.md)
- [Test Driven Development](0x07-python-test_driven_development/README.md)
___

- [JavaScript: Warm Up](0x12-javascript-warm_up/README.md)
- [JavaScript: Objects, Scopes, Closures](0x13-javascript_objects_scopes_closures/README.md)
- [JavaScript: Web Scrapping](0x14-javascript-web_scraping/README.md)
- [JavaScript: Web jQuery](0x15-javascript-web_jquery/README.md)
___

- [SQL: Introduction](0x0D-SQL_introduction/README.md)
- [SQL: More Queries](0x0E-SQL_more_queries/README.md)
___

- [Requirements](#requirements)

# Description

## Concepts

*For this project, we expect you to look at this concept:*

[Python programming](https://intranet.alxswe.com/concepts/550)

## Author’s disclaimer

![Python](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)

```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.

Enjoy!

- Guillaume
```

# Resources

**Read or watch:**
- [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (*only the first three chapters below*)
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (*Read up until “3.1.2. Strings” included*)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google:**

## General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

# Requirements

## Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

## Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### Documentation
- Do not use the words `import` or `from` inside your comments, the checker will think you try to import some modules

### .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

### Shell Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

### C Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/alx-tools/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/alx-tools/Betty/blob/master/betty-doc.pl)
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## More Info

**Zen**

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

**Pycodestyle**
`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

![Monty](images/monty.jpeg)

## Author

**Tafara Nyamhunga - [Github](https://github.com/tafara-n) / [Twitter](https://twitter.com/tafaranyamhunga)**
