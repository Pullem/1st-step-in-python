import sys


import PyQt5.QtWidgets

import qdarkstyle
import PyQt5.QtWidgets


class Example(PyQt5.QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		grid = PyQt5.QtWidgets.QGridLayout()
		self.setLayout(grid)

		# list = []     names = [list-item_0, list-item_1, list-item_3, ......]
		# The list comprehension starts with a '[' and ends with a ']',
		# to help you remember that the result is going to be a list.   - gerd
		names = ['Cls', 'Bck', '', 'Close',
			 '7', '8', '9', '/',
			'4', '5', '6', '*',
			 '1', '2', '3', '-',
			'0', '.', '=', '+']

		positions = [(i, j) for i in range(5) for j in range(4)]

		# 'zip' = With zip we can act upon two lists at once.
		# Zip() is a built-in function.
		# We pass it two iterables, like lists, and it enumerates them together.
		# Here we have two string lists, 'names' and 'positions'.
		# We use zip on the two lists. we step (iterate) through these lists in parallel,
		# we combine element_0 of the first list and element_0 of the second list
		# 'position'-element is 'row' and 'column' : first list-element 0,0  ( i and j ),
		# and first list-element of 'names' is 'Cls'
		# QPushButton will position the first button at row_0 and column_0 with the name_0 label
		# at line 53 the star * (*position) unpacks the sequence '0, 0' into positional arguments
		# 'row' and 'column' for the 'addWidget(button, row, column)'
		for position, name in zip(positions, names):

			# with this 'print' we can follow the 'range' flows
			# both starts with 0 , and exits/breaks, when the pyhton-internal counters
			# have reached the given endpoint : '5' for 'i' , or/and '4' for 'j'    - gerd
			# print("this is 'name': ", name, "   and these are the 'position' for 'i' and 'j': ", position)
			print("this is the 'zip-position' for 'i' and 'j': ", position, "and this is 'zip-name': ", name)

			if name == '':      # nothing between - no white space !   - gerd
				continue
			button = PyQt5.QtWidgets.QPushButton(name)
			grid.addWidget(button, *position)
			
		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Calculator')
		self.show()

if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

# grid.addWidget(button, *position)
'''
the position (i,j) refers to (row, column)
'''