import sys
import qdarkstyle

# original import: from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QDesktopWidget)
# PyCharm says:
import PyQt5.QtWidgets
# and so on:
import PyQt5.QtGui
import PyQt5.QtCore

class Example(PyQt5.QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont('Open Sans', 8))

		# btn = PyQt5.QtWidgets.QPushButton('Quit', self)
		# width of button automaticaly adapted:
		btn = PyQt5.QtWidgets.QPushButton('Quit or sth else and more', self)
		print("btn = ", btn)
		# here we connect a kind of cable:
		# from 'btn' , our QPushButton, to the running instance, and transfer 'quit' when clicked
		btn.clicked.connect(PyQt5.QtCore.QCoreApplication.instance().quit)
		# in the next line '\n' means 'new line' :
		# btn.setToolTip('Quits the \nApplication')
		btn.setToolTip('First Line \nSecond Line')
		btn.resize(btn.sizeHint())
		btn.move(50,50)

		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Centering Window on Desktop')
		self.setWindowIcon(PyQt5.QtGui.QIcon('./../fugue_icons/construction.png'))
		# print(./)
		self.center()

		self.show()

	def center(self):
		win_geo = self.frameGeometry()
		print("win_geo: ", win_geo)
		center_point = PyQt5.QtWidgets.QDesktopWidget().availableGeometry().center()
		# with my display 1680 x 1050 pixels, it says: 839 , 504 ?? without windows task-line ??
		print("... and the 'center_point' is : ", center_point)
		win_geo.moveCenter(center_point)
		self.move(win_geo.topLeft())

if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
The QtGui.QDesktopWidget class provides information about the user's desktop, 
including the screen size.
'''

# self.center()
'''
The code that will center the window is placed in the custom center() method.
'''

# win_geo = self.frameGeometry()
'''
We get a rectangle specifying the geometry of the app main window. 
This includes any window frame.
'''

# center_point = QDesktopWidget().availableGeometry().center()
'''
We figure out the screen resolution of our monitor. 
And from this resolution, we get the center point.
'''

# win_geo.moveCenter(centerPoint)
'''
Our rectangle has already its width and height. 
Now we set the center of the rectangle to the center of the screen. 
The rectangle's size is unchanged.
'''

# self.move(win_geo.topLeft())
'''
We move the top-left point of the application window to the top-left point 
of the qr rectangle, thus centering the window on our screen.
'''