# 1st-step-in-python
My way to learn python and pyqt5

I don't like books (epub, pdf), start with page 001 and read until 256
just examine the code of a useful python script, this is my way

Examples with many notes and remarks from 'alvin lam' !!

and some, intended, from me, gerd , but don't believe what you read: 
this is my understanding of these sources,  and it may be wrong !!!

win 10pro 64bit
python 3.5 / pyqt 5.7
My ide is JetBrains PyCharm Community Edition 2016.2

## icons
icons i use: **fugue-icons** here from github

## import
from ... import ... 
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

## class

We define a class in the following way
class nameoftheclass(parent_class):



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

