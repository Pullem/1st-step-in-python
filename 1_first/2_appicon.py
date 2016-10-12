import sys
import qdarkstyle

# original import: from PyQt5.QtWidgets import QApplication, QWidget
# PyCharm says:     - gerd
import PyQt5.QtWidgets
# and so on:
import PyQt5.QtGui


# class nameoftheclass(parent_class):   - gerd
class Example(PyQt5.QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('<< App Icon !!')
		# self.setWindowIcon(PyQt5.QtGui.QIcon('./Icons/gxs-256.ico'))
		# self.setWindowIcon(PyQt5.QtGui.QIcon(r'.\Icons\battery-full.png'))
		self.setWindowIcon(PyQt5.QtGui.QIcon('.\..\\fugue_icons\\battery-full.png'))
# obove, both lines work for me:  / or \  ??, i believed it depends on the operating system ?
# take notice of the 'r' in front of the path to battery-full
# we have the character string ...ons\batte.... ; the combination '\b' is a special character:
# \n = newline , \b = backspace , \f = ... , some more
# i believe python is looking for '\Iconattery-full.png'
# 'r' means 'raw' : escape character '\' will be ignored ; alternative double '\'     - gerd

		self.show()

if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
# the next line is a call of our class 'Example', and generates an instance of an 'object'   ?????
	ex = Example()
	print(ex)
	sys.exit(app.exec_())


# class Example(QWidget):
#    def __init__(self):
#        super().__init__()
'''Here we create a new class called Example. The Example class inherits 
	from the QWidget class. This means that we call two constructors: 
	the 1st one for the Example class and the 2nd one for the inherited class. 
	The super() method returns the parent object of the Example class and we 
	call its constructor. 
	The __init__() method is a constructor method in Python language.
'''

# self.init_ui()
'''The creation of the GUI is delegated to the init_ui() method.'''

# self.setGeometry(300, 300, 300, 220)
# self.setWindowTitle('Icon')
# self.setWindowIcon(QIcon('web.png'))
'''All three methods have been inherited from the QWidget class. 
	The setGeometry() does two things: it locates the window on the screen 
	and sets it size. The first two parameters are the x and y positions 
	of the window. 
	The third is the width and the fourth is the height of the window. 
	In fact, it combines the move() then resize() methods in one method. 
	
	The last method sets the application icon. To do this, we have created a 
	QIcon object. The QIcon receives the path to our icon to be displayed.
'''

# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())
'''The application and example objects are created. The main loop is started.'''
