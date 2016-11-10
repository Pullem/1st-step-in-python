import sys
import qdarkstyle
import PyQt5.QtWidgets

class Example(PyQt5.QtWidgets.QWidget):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		title = PyQt5.QtWidgets.QLabel('Title')
		author = PyQt5.QtWidgets.QLabel('Author')
		review = PyQt5.QtWidgets.QLabel('Review')

		# QLineEdit: only one line, no auto expansion to two, three, ... llines
		title_edit = PyQt5.QtWidgets.QLineEdit("title edit")

		# QTextEdit: auto expansion, if box full, with vertical scrollbar
		author_edit = PyQt5.QtWidgets.QTextEdit()
		review_edit = PyQt5.QtWidgets.QTextEdit()

		grid = PyQt5.QtWidgets.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(title, 1, 0)
		grid.addWidget(title_edit, 1, 1)

		grid.addWidget(author, 2, 0)
		author_edit.setSizePolicy(PyQt5.QtWidgets.QSizePolicy.Ignored,
		                         PyQt5.QtWidgets.QSizePolicy.Ignored)
		grid.addWidget(author_edit, 2, 1, 2, 1)

		grid.addWidget(review, 8, 0)
		grid.addWidget(review_edit, 8, 1, 5, 1)

		self.setLayout(grid)

		self.setGeometry(300,300, 350, 300)
		self.setWindowTitle('Multiple grids')
		self.show()

if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

# grid = QGridLayout()
# grid.setSpacing(10)
'''We create a grid layout and set spacing between widgets.'''

# grid.addWidget(reviewEdit, 3, 1, 5, 1)
'''
If we add a widget to a grid, we can provide row and column span of the widget. 
In our case, we make the reviewEdit widget span 5 rows.
'''