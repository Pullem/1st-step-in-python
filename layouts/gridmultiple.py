import sys
import qdarkstyle
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QGridLayout,
	QLabel, QLineEdit, QTextEdit, QSizePolicy)

class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		title = QLabel('Title')
		author = QLabel('Author')
		review = QLabel('Review')

		titleEdit = QLineEdit()
		authorEdit = QTextEdit()
		reviewEdit = QTextEdit()

		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(title, 1, 0)
		grid.addWidget(titleEdit, 1, 1)

		grid.addWidget(author, 2, 0)
		authorEdit.setSizePolicy(QSizePolicy.Ignored,
            QSizePolicy.Ignored)
		grid.addWidget(authorEdit, 2, 1, 2, 1)

		grid.addWidget(review, 8, 0)
		grid.addWidget(reviewEdit, 8, 1, 5, 1)

		self.setLayout(grid)

		self.setGeometry(300,300, 350, 300)
		self.setWindowTitle('Multiple grids')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
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