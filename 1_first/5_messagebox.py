import sys
import qdarkstyle
import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore


class Example(PyQt5.QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont('Open Sans', 10))

		btn = PyQt5.QtWidgets.QPushButton('Quit', self)
		btn.clicked.connect(PyQt5.QtCore.QCoreApplication.instance().quit)
		btn.setToolTip('Quits the \nApplication')
		btn.resize(btn.sizeHint())
		btn.move(50, 50)

		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Message Box on Close')
		self.setWindowIcon(PyQt5.QtGui.QIcon('./Icons/gxs-256.ico'))

		self.show()

	def closeEvent(self, event):
		reply = PyQt5.QtWidgets.QMessageBox.question(self, 'Message',
		                                             "Are you sure\nyou want to quit?",
		                                             PyQt5.QtWidgets.QMessageBox.Yes |
		                                             PyQt5.QtWidgets.QMessageBox.No, PyQt5.QtWidgets.QMessageBox.No)

		if reply == PyQt5.QtWidgets.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

# reply = QMessageBox.question(self, 'Message',
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

# if reply == QtGui.QMessageBox.Yes:
#    event.accept()
# else:
#    event.ignore()
'''
Here we test the return value. If we click the Yes button, 
we accept the event which leads to the closure of the widget and to 
the termination of the application. Otherwise we ignore the close event.
'''

# 	def closeEvent(self, event):        - gerd
'''
this def !! overwrites !! the original from QWindow
the x in the top-right corner of our window, NOT the just generated "quit" -button
'''