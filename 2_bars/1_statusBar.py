import sys
import PyQt5.QtWidgets
import qdarkstyle


class StatBar(PyQt5.QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		self.statusBar().showMessage('Statusbar is here')

# The setGeometry() does two things:
# it locates the window on the screen and sets it size.
# The first two parameters are the x and y positions of the window.
# The third is the width and the fourth is the height of the window.
# In fact, it combines the resize() and move() methods in one method        - gerd
		self.setGeometry(500, 300, 250, 150)
		self.setWindowTitle('StatusBar')
		self.show()


if __name__ == '__main__':
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	stat = StatBar()
	sys.exit(app.exec_())

# self.statusBar().showMessage('Ready')
'''
statusBar() from QMainWindow, first call creates status bar, 
sesequent calls returns the statusBar
showMessage() displays a message on statusBar()
'''
