# 1st-step-in-python
My way to learn python and pyqt5

I don't like books (epub, pdf), start with page 001 and read until 256
just examine the code of a useful python script, this is my way

Examples with many notes and remarks from 'Alvin Lam' !!

and some from me, Gerd , but don't believe what you read: 
this is my understanding of these sources,  and it may be wrong !!!

win 10pro 64bit
WinPython-64bit-3.5.2.1Qt5\python-3.5.2.amd64
My ide is JetBrains PyCharm Community Edition 2016.2

## icons
icons i use: **fugue-icons** here from github

## import
from ... import ... 

**Importing Modules**

**description a:**
put it in a nutshell: every file, which has the file extension .py and consists of proper Python code, can be seen or is a module! 
There is no special syntax required to make such a file a module. A module can contain arbitrary objects, for example files, classes or attributes. 
All those objects can be accessed after an import. There are different ways to import a modules. 
We demonstrate this with the math module:   [importing modules](http://www.python-course.eu/python3_modules_and_modular_programming.php)
import math

**description b:**
Using 'from modul import func' is a way to pinpoint the function you want to import and put it in the global namespace. 
While much less harmful than import * because it shows explicitly what is imported in the global namespace, 
its only advantage over a simpler import modu is that it will save a little typing.
examples from [here](http://docs.python-guide.org/en/latest/writing/structure/)

**Very bad**
[...]
from modu import *
[...]
x = sqrt(4)  # Is sqrt part of modu? A builtin? Defined above?

**Better**
from modu import sqrt
[...]
x = sqrt(4)  # sqrt may be part of modu, if not redefined in between

**Best**
import modu
[...]
x = modu.sqrt(4)  # sqrt is visibly part of modu's namespace
this is also the suggestion of PyCharm


**if __name__ == '____main____':**
When the Python interpreter reads a source file ( or better: "imports a source file" ), it executes all of the code found in it.
Before executing the code, it will define a few special variables. 
For example, if the python interpreter is running that module (the source file) as the main program, 
it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, 
__name__ will be set to the module's name.

One of the reasons for doing this is that sometimes you write a module (a .py file) where it can be executed directly. 
Alternatively, it can also be imported and used in another module. 
By doing the main check, you can have that code only execute when you want to run the module as a program and 
not have it execute when someone just wants to import your module and call your functions themselves.

see [What does `if __name__ == “__main__”:` do?](http://stackoverflow.com/questions/419163/what-does-if-name-main-do) or [this](http://thepythonguru.com/what-is-if-__name__-__main__/)


## class

We define a class in the following way

+ class nameoftheclass(parent_class):



## def

**description a:**
You define functions in Python using the **def** keyword. The form looks like this:

+ def functionName(parameter1, param2,...):     followed by the
+ function block

Python functions always return a value. You can specify an explicit return value using the **return**
keyword; otherwise, Python returns None by default.

**description b:**
A function in Python is defined by using the **def** keyword, after which the **name of the function** follows,
terminated by **a pair of braces** (which may or may not contain input parameters) and,
finally, a colon (:) signals the end of the function definition line.
Immediately afterwards, **indented by four spaces**, we find the body of the function, which
is the set of instructions that the function will execute when called.

A function may or may not return output. If a function wants to return output,
it does so by using the return keyword, followed by the desired output.
( If you have an eagle eye, you may have noticed the little * after Optional
in the output section of the preceding picture.
This is because a function always returns something in Python, even if you don’t explicitly use the return clause.
If the function has no return statement in its body, it’s return value is None. )


## PyQt5

more information [PyQt5 Reference Guide](http://pyqt.sourceforge.net/Docs/PyQt5/index.html)

e.g. for '1_first.py'
in **quick search**: QWidget  ; one answer is 'PyQt5.QtWidgets.QWidget' ,
left mouse click and than you will find a pointer to the C++ doc, scroll down
**Public Functions** and here you find more information to 'resize' 'move' ... :

[learn more here](http://zetcode.com/gui/pyqt4/firstprograms/) or
[here](https://pythonprogramming.net/basic-gui-pyqt-tutorial/)
