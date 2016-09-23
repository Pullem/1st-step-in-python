import sys
import qdarkstyle
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
	QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      

		vbox = QVBoxLayout()

		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Fixed,
			QSizePolicy.Fixed)
		
		btn.move(20, 20)

		vbox.addWidget(btn)

		btn.clicked.connect(self.showDialog)
		
		self.lbl = QLabel('Knowledge only matters', self)
		self.lbl.move(130, 20)

		vbox.addWidget(self.lbl)
		self.setLayout(vbox)          
		
		self.setGeometry(300, 300, 250, 180)
		self.setWindowTitle('Font dialog')
		self.show()
		
		
	def showDialog(self):

		font, ok = QFontDialog.getFont()
		if ok:
			self.lbl.setFont(font)
		
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
In our example, we have a button and a label. 
With the QFontDialog, we change the font of the label.
'''

# font, ok = QFontDialog.getFont()
'''
Here we pop up the font dialog. 
The getFont() method returns the font name and the ok parameter. 
It is equal to True if the user clicked OK; otherwise it is False.
'''

# if ok:
#     self.label.setFont(font)
'''
If we clicked Ok, the font of the label would be changed.
'''