import sys
import qdarkstyle
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
	QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      

		col = QColor(0, 0, 0) 

		self.btn = QPushButton('Dialog', self)
		self.btn.move(20, 20)

		self.btn.clicked.connect(self.showDialog)

		self.frm = QFrame(self)
		self.frm.setStyleSheet("QWidget { background-color: %s }" 
			% col.name())
		self.frm.setGeometry(130, 22, 100, 100)            
		
		self.setGeometry(300, 300, 250, 180)
		self.setWindowTitle('Color dialog')
		self.show()
		
		
	def showDialog(self):
	  
		col = QColorDialog.getColor()

		if col.isValid():
			self.frm.setStyleSheet("QWidget { background-color: %s }"
				% col.name())
			
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())


'''
The application example shows a push button and a QFrame. 
The widget background is set to black colour. 
Using the QColorDialog, we can change its background.
'''

# col = QColor(0, 0, 0) 
'''
This is an initial colour of the QtGui.QFrame background.
'''

# col = QColorDialog.getColor()
'''
This line will pop up the QColorDialog.
'''

# if col.isValid():
#     self.frm.setStyleSheet("QWidget { background-color: %s }"
#         % col.name())
'''
We check if the colour is valid. 
If we click on the Cancel button, no valid colour is returned. 
If the colour is valid, we change the background colour using style sheets.
'''