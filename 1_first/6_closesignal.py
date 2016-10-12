import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
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
		self.setWindowTitle('Close Signal')
		self.setWindowIcon(QIcon('./Icons/gxs-256.ico'))

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

# from PyQt5.QtCore import QCoreApplication
'''We need an object from the QtCore module.'''

# btn = QPushButton('Quit', self)
'''
We create a push button. The button is an instance of the QPushButton class.
The first parameter of the constructor is the label of the button. 
The second parameter is the parent widget. 
The parent widget is the Example widget, which is a QWidget by inheritance.
'''

# btn.clicked.connect(QCoreApplication.instance().quit)
'''
The event processing system in PyQt5 is built with the signal & slot mechanism.
If we click on the button, the signal clicked is emitted. 
The slot can be a Qt slot or any Python callable. 
The QCoreApplication contains the main event loop; it processes and 
dispatches all events. The instance() method gives us its current instance.
Note that QCoreApplication is created with the QApplication. 
The clicked signal is connected to the quit() method which terminates 
the application. The communication is done between two objects: 
the sender and the receiver. 
The sender is the push button, the receiver is the application object.
'''