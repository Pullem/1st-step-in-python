import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon 

class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Icon App')
		self.setWindowIcon(QIcon('./Icons/gxs-256.ico'))

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())


#class Example(QWidget):
#    def __init__(self):
#        super().__init__()
'''Here we create a new class called Example. The Example class inherits 
	from the QWidget class. This means that we call two constructors: 
	the 1st one for the Example class and the 2nd one for the inherited class. 
	The super() method returns the parent object of the Example class and we 
	call its constructor. 
	The __init__() method is a constructor method in Python language.
'''

#self.init_ui()
'''The creation of the GUI is delegated to the init_ui() method.'''

#self.setGeometry(300, 300, 300, 220)
#self.setWindowTitle('Icon')
#self.setWindowIcon(QIcon('web.png'))
'''All three methods have been inherited from the QWidget class. 
	The setGeometry() does two things: it locates the window on the screen 
	and sets it size. The first two parameters are the x and y positions 
	of the window. 
	The third is the width and the fourth is the height of the window. 
	In fact, it combines the move() then resize() methods in one method. 
	
	The last method sets the application icon. To do this, we have created a 
	QIcon object. The QIcon receives the path to our icon to be displayed.
'''

#app = QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())
'''The application and example objects are created. The main loop is started.'''