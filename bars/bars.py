import sys
import PyQt5.QtWidgets
import PyQt5.QtGui
import qdarkstyle


# class nameoftheclass(parent_class):
class Example(PyQt5.QtWidgets.QMainWindow):
	# functionname __init__
	def __init__(self):
		super().__init__()
		
		self.init_ui()
		# print(self.init_ui)

	def init_ui(self):
		# textedit widget, centralwidget set to text edit (occupy all space remaining)
		text_edit = PyQt5.QtWidgets.QTextEdit()
		self.setCentralWidget(text_edit)

# of course, this path to 'appbar.close.png' doesn't exist, therefor modyfy this line for our environment.
# with the original line:
# no error at execution of this script, but, in the gui, move your mouse under the menueitem 'file' ( a bit right),
# and you will see only a blue frame without icon
		exit_action = PyQt5.QtWidgets.QAction(
			# PyQt5.QtGui.QIcon('.\..\..\Tools\WindowsIcons-master\WindowsPhone\dark\/appbar.close.png'), 'Exit', self)
			PyQt5.QtGui.QIcon('.\Icons\cross.png'), 'Exit', self)
		exit_action.setShortcut('Ctrl+Q')
		exit_action.setStatusTip('Exit application')
		exit_action.triggered.connect(self.close)

		self.statusBar()

		menubar = self.menuBar()
		file_menu = menubar.addMenu('&File')
		file_menu.addAction(exit_action)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exit_action)
		
		self.setGeometry(300, 300, 350, 250)
		self.setWindowTitle('Main window')    
		self.show()
		
		
if __name__ == '__main__':
	
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())
