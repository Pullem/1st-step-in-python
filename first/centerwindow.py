import sys
import qdarkstyle
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, 
	QDesktopWidget)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('Open Sans', 8))

		btn = QPushButton('Quit', self)
		btn.clicked.connect(QCoreApplication.instance().quit)
		btn.setToolTip('Quits the \nApplication')
		btn.resize(btn.sizeHint())
		btn.move(50,50)

		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Centering Window on Desktop')
		self.setWindowIcon(QIcon('./Icons/gxs-256.ico'))
		self.center()

		self.show()

	def center(self):
		winGeo = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		winGeo.moveCenter(centerPoint)
		self.move(winGeo.topLeft())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
The QtGui.QDesktopWidget class provides information about the user's desktop, 
including the screen size.
'''

#self.center()
'''
The code that will center the window is placed in the custom center() method.
'''

#winGeo = self.frameGeometry()
'''
We get a rectangle specifying the geometry of the app main window. 
This includes any window frame.
'''

#centerPoint = QDesktopWidget().availableGeometry().center()
'''
We figure out the screen resolution of our monitor. 
And from this resolution, we get the center point.
'''

#winGeo.moveCenter(centerPoint)
'''
Our rectangle has already its width and height. 
Now we set the center of the rectangle to the center of the screen. 
The rectangle's size is unchanged.
'''

#self.move(winGeo.topLeft())
'''
We move the top-left point of the application window to the top-left point 
of the qr rectangle, thus centering the window on our screen.
'''