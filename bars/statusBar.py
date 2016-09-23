import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import qdarkstyle

class statBar(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.statusBar().showMessage('Ready')

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('StatusBar')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	stat = statBar()
	sys.exit(app.exec_())

#self.statusBar().showMessage('Ready')
'''
statusBar() from QMainWindow, first call creates status bar, 
sesequent calls returns the statusBar
showMessage() displays a message on statusBar()
'''