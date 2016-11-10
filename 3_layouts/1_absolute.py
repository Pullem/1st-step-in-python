import sys
import qdarkstyle
import PyQt5.QtWidgets

class Example(PyQt5.QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		label1 = PyQt5.QtWidgets.QLabel('PyQt5', self)
		label1.move(15, 10)

		label2 = PyQt5.QtWidgets.QLabel('test tutorials', self)
		label2.move(35,40)

		label3 = PyQt5.QtWidgets.QLabel('for new users', self)
		label3.move(55, 70)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Absolute Layout')
		self.show()

if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
We use the move() method to position our widgets. In our case these are labels.
We position them by providing the x and y coordinates. 
The beginning of the coordinate system is at the left top corner. 
The x values grow from left to right. The y values grow from top to bottom.

when we resize the window, with left-pushed mouse at the bottom right corner,
our three text lines remain on their positions   - gerd

'''