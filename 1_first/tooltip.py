import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QIcon, QFont

class Example(QWidget):

	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('Open Sans', 8))

		self.setToolTip('This is a <b>QWidget</b> widget')

		btn = QPushButton('Button', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(50,50)

		self.setGeometry(300, 300, 300, 220)
		self.setWindowTitle('Tool Tip')
		self.setWindowIcon(QIcon('./Icons/gxs-256.ico'))

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

#QToolTip.setFont(QFont('SansSerif', 10))
'''static method sets a font for tooltips. We use a 8px Open Sans font.'''

#self.setToolTip('This is a <b>QWidget</b> widget')
'''To create a tooltip, we call setTooltip(). Can rich text formatting.'''

#btn = QPushButton('Button', self)
#btn.setToolTip('This is a <b>QPushButton</b> widget')
'''We create a push button widget and set a tooltip for it.'''

#btn.resize(btn.sizeHint())
#btn.move(50, 50)
'''The button is being resized and moved on the window. 
	The sizeHint() method gives a recommended size for the button.'''