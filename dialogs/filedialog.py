import sys
import qdarkstyle
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
	QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      

		self.textEdit = QTextEdit()
		self.setCentralWidget(self.textEdit)
		self.statusBar()

		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)       
		
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('File dialog')
		self.show()
		
		
	def showDialog(self):

		fname = QFileDialog.getOpenFileName(self, 'Open file')
		
		self.textEdit.setText(str(fname)) 
								
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	
	ex = Example()
	sys.exit(app.exec_())

'''
The example shows a menubar, centrally set text edit widget, and a statusbar.
The menu item shows the QtGui.QFileDialog which is used to select a file. 
The contents of the file are loaded into the text edit widget.
'''

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
'''
The example is based on the QMainWindow widget 
because we centrally set a text edit widget.
'''

# fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
'''
We pop up the QFileDialog. The first string in the getOpenFileName() 
method is the caption. The second string specifies the dialog working directory
By default, the file filter is set to All files (*).
'''

# f = open(fname, 'r')
# with f:        
#     data = f.read()
#     self.textEdit.setText(data) 
''' 
The selected file name is read and the contents 
of the file are set to the text edit widget.
'''