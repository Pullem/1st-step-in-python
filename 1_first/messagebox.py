import sys
import qdarkstyle
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, 
	QMessageBox)
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
		self.setWindowTitle('Message Box on Close')
		self.setWindowIcon(QIcon('./Icons/gxs-256.ico'))

		self.show()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message', 
			"Are you sure\nyou want to quit?", QMessageBox.Yes |
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

#reply = QMessageBox.question(self, 'Message',
#    "Are you sure you want to quit?", QMessageBox.Yes | 
#    QMessageBox.No, QMessageBox.No)
'''
We show a message box with two buttons: Yes and No. 
The first string appears on the titlebar. 
The second string is the message text displayed by the dialog. 
The third argument specifies the combination of buttons appearing in the dialog
The last parameter is the default button. It is the button which has initially 
the keyboard focus. The return value is stored in the reply variable.
'''

#if reply == QtGui.QMessageBox.Yes:
#    event.accept()
#else:
#    event.ignore()
'''
Here we test the return value. If we click the Yes button, 
we accept the event which leads to the closure of the widget and to 
the termination of the application. Otherwise we ignore the close event.
'''