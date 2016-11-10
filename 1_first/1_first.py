#creating a sample window in PyQt5

import sys
import PyQt5.QtWidgets
# 'QtWidgets' contains classes that provide a set of UI elements
# to create classic desktop-style user interfaces.

import qdarkstyle

# let us print our variables:   - gerd
#
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

# and where is our Python interpreter ?
print("our interpreter is here: ", sys.executable)

if __name__ == '__main__':
	# see README
	print("1_first.py is being run directly")
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	print("This is 'app': ", app)
#	print(sys.argv)
# comment the following line, and see the differences in gui-colour  - gerd
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	w = PyQt5.QtWidgets.QWidget()
	w.resize(250, 150)
	w.move(100, 100)
	w.setWindowTitle('First')
	w.show()

# can we open a second window ?
	w2 = PyQt5.QtWidgets.QWidget()
	w2.resize(350, 50)
	w2.move(300, 300)
	w2.setWindowTitle('Second')
	w2.show()

	sys.exit(app.exec_())

# app = QApplication(sys.argv)
# Every PyQt5 application must create an application object.

# The 'sys.argv' parameter is a list of arguments from a command line.
	# sys — System-specific parameters and functions; see obove: you have imported 'sys'
	# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
	# If you are gonna work with command line arguments, you probably want to use sys.argv.
	# (From the view of python:
	# Remember that sys.argv[0] is the name of the script and therefor the first argument, we count from 0
	# CLI:  python.exe 1_first.py  - gerd )
	#
	# This module provides access to some variables used or maintained by the interpreter and to functions
	# that interact strongly with the interpreter. It is always available.


# w = QWidget()   -   or, in this example, with the suggestions of PyCharm:
	# w = PyQt5.QtWidgets.QWidget()
	# this is an assignment for 'w' , because you don't like to type 'PyQt5.QtWidg....' - gerd
# The QWidget widget is the base class of all user interface objects in PyQt5.
# The default constructor has no parent. A widget with no parent is  a window.

# w.resize(250, 150)
# resizes the widget. It is 250px wide and 150px high.

# w.move(300, 300)
# moves the widget to a position on the screen at x=300, y=300 coordinates.

# w.setWindowTitle('Simple')
# set the title for our window. The title is shown in the titlebar.

# w.show()
# displays the widget on the screen. Widgets are first created in memory

# sys.exit(app.exec_())
# we enter the mainloop of the application.
# The event handling starts from this point. sys.exit() ensures a clean exit
#   Using sys.exit() with app.exec_ in pyqt:    -   stackoverflow com questions/25075954/using-sys-exit-with-app-exec-in-pyqt
#   When Unix-style applications exit, they return a number to their parent process called a 'status code' or 'exit status'.
#   0 is used to indicate success; anything non-zero is a failure.
#   (There's been some attempt to standardise the meaning of error codes, but it's still generally left up to each program.)
#   app.exec_() runs your main loop, and returns a status code when it exits.
#   sys.exit(n) quits your application and returns n to the parent process (normally your shell).
#   So the difference is, the longer version passes on the status code when your program exits.
#   It's better to use sys.exit(app.exec_()) because then other parts of the system can detect when your program exited due to an error.
#
#   app.exec_() returns either 0 for success or an error message if it crashed
#   sys.exit(n) returns the value n to the parent process (normally your shell)
#   So if you call them separately and the app.exec_() crashes, the shell never receives the error code.
#   the internal function is called first. This would yield the same result:
#   status = app.exec_()
#   sys.ext(status)
