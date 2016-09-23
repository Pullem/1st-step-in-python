import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction
from PyQt5.QtGui import QIcon
import qdarkstyle

class Example(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		#textedit widget, centralwidget set to text edit (occupy all space remaining)
		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)

		exitAction = QAction(QIcon('.\..\..\Tools\WindowsIcons-master\WindowsPhone\dark\/appbar.close.png'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAction)
		
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Main window')    
		self.show()
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())