import sys
import qdarkstyle
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
	QApplication)

class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		okButton = QPushButton('OK')
		cancelButton = QPushButton('Cancel')

		hbox = QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)

		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)

		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('box layout buttons')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
The example places two buttons in the bottom-right corner of the window. 
They stay there when we resize the application window. 
We use both a HBoxLayout and a QVBoxLayout.
'''

# hbox = QHBoxLayout()
# hbox.addStretch(1)
# hbox.addWidget(okButton)
# hbox.addWidget(cancelButton)
'''
We create a horizontal box layout and add a stretch factor and both buttons. 
The stretch adds a stretchable space before the two buttons. 
This will push them to the right of the window.
'''

# vbox = QVBoxLayout()
# vbox.addStretch(1)
# vbox.addLayout(hbox)
'''
To create the necessary layout, we put a horizontal layout into a vertical one.
The stretch factor in the vertical box will push the horizontal box 
with the buttons to the bottom of the window.
'''

#self.setLayout(vbox)
'''Finally, we set the main layout of the window.'''