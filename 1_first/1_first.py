#creating a sample window in PyQt5

import sys
import PyQt5.QtWidgets
import qdarkstyle

# let us print our variables:   - gerd
#
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	w = PyQt5.QtWidgets.QWidget()
	w.resize(250, 150)
	w.move(300, 300)
	w.setWindowTitle('Simple')
	w.show()

	sys.exit(app.exec_())

# app = QApplication(sys.argv)
# Every PyQt5 application must create an application object.
# The sys.argv parameter is a list of arguments from a command line.
	# sys — System-specific parameters and functions; see obove: you have imported 'sys'
	# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
	# If you are gonna work with command line arguments, you probably want to use sys.argv.
	# (From the view of python:
	# Remember that sys.argv[0] is the name of the script and therefor the first argument, we count from 0
	# CLI:  python.exe 1_first.py)  - gerd
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
