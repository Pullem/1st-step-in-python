import sys
import qdarkstyle
import PyQt5.QtWidgets
import PyQt5.QtGui


class Example(PyQt5.QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		col = PyQt5.QtGui.QColor(0, 0, 0)

		self.btn = PyQt5.QtWidgets.QPushButton('Dialog', self)
		self.btn.move(20, 20)

		self.btn.clicked.connect(self.show_dialog)

		self.frm = PyQt5.QtWidgets.QFrame(self)
		self.frm.setStyleSheet("QWidget { background-color: %s }"
		                       % col.name())
		self.frm.setGeometry(130, 22, 100, 100)

		self.setGeometry(300, 300, 250, 180)
		self.setWindowTitle('Color dialog')
		self.show()

	def show_dialog(self):
		col = PyQt5.QtWidgets.QColorDialog.getColor()
		print(col.name)

		if col.isValid():
			self.frm.setStyleSheet("QWidget { background-color: %s }"
			                       % col.name())

		print("QWidget { background-color: %s }"% col.name())


if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	print(app)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
The application example shows a push button and a QFrame. 
The widget background is set to black colour. 
Using the QColorDialog, we can change its background.
'''

# col = QColor(0, 0, 0) 
'''
This is an initial colour of the QtGui.QFrame background.
'''

# col = QColorDialog.getColor()
'''
This line will pop up the QColorDialog.
'''

# if col.isValid():
#     self.frm.setStyleSheet("QWidget { background-color: %s }"
#         % col.name())
'''
We check if the colour is valid. 
If we click on the Cancel button, no valid colour is returned. 
If the colour is valid, we change the background colour using style sheets.
'''
