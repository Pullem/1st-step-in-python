import sys
import PyQt5.QtWidgets
import PyQt5.QtGui
import qdarkstyle


class ExampleMenu(PyQt5.QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		exitAction = PyQt5.QtWidgets.QAction(PyQt5.QtGui.QIcon('./Icons/cross.png'), '&Exit - item of file', self)
		exitAction.setShortcut('Ctrl+Q')
		# which characters will be accepted ??
		# exitAction.setShortcut('Shortcut: Ctrl+Q')
		exitAction.setStatusTip('Statusbar: Quit the Application')
		exitAction.triggered.connect(PyQt5.QtWidgets.qApp.quit)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('File')
		fileMenu.addAction(exitAction)

		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Menubar')
		self.show()

if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = ExampleMenu()

	sys.exit(app.exec_())