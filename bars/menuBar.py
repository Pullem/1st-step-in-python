import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
import qdarkstyle

class ExampleMenu(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		exitAction = QAction(QIcon('./Icons/close.png'), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Quit the Application')
		exitAction.triggered.connect(qApp.quit)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('File')
		fileMenu.addAction(exitAction)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Menubar')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = ExampleMenu()

	sys.exit(app.exec_())