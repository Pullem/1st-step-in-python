import sys
import PyQt5.QtWidgets
import PyQt5.QtGui
import qdarkstyle

class Example(PyQt5.QtWidgets.QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):               
		exitAction = PyQt5.QtWidgets.QAction(
			PyQt5.QtGui.QIcon('./Icons/cross.png'), 'Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.triggered.connect(PyQt5.QtWidgets.qApp.quit)
		
		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAction)
		
		self.setGeometry(300, 300, 300, 200)
		self.setWindowTitle('Toolbar')    
		self.show()
		
		
if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

# we can move this toolbar to all sides of our window:
# just move the two parallel vertical lines left of the red cross