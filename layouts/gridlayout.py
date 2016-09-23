import sys
import qdarkstyle
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QGridLayout)

class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		self.setLayout(grid)

		names = ['Cls', 'Bck', '', 'Close',
			 '7', '8', '9', '/',
			'4', '5', '6', '*',
			 '1', '2', '3', '-',
			'0', '.', '=', '+']

		positions = [(i,j) for i in range(5) for j in range(4)]
		
		for position, name in zip(positions, names):
			
			if name == '':
				continue
			button = QPushButton(name)
			grid.addWidget(button, *position)
			
		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Calculator')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

# grid.addWidget(button, *position)
'''
the position (i,j) refers to (row, column)
'''