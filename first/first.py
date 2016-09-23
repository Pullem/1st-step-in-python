#creating a sample window in PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QWidget
import qdarkstyle

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	w = QWidget()
	w.resize(250, 150)
	w.move(300, 300)
	w.setWindowTitle('Simple')
	w.show()

	sys.exit(app.exec_())

#app = QApplication(sys.argv)
#Every PyQt5 application must create an application object. 
#The sys.argv parameter is a list of arguments from a command line.

#w = QWidget()
#The QWidget widget is the base class of all user interface objects in PyQt5. 
#The default constructor has no parent. A widget with no parent is  a window.

#w.resize(250, 150)
#resizes the widget. It is 250px wide and 150px high.

#w.move(300, 300)
#moves the widget to a position on the screen at x=300, y=300 coordinates.

#w.setWindowTitle('Simple')
#set the title for our window. The title is shown in the titlebar.

#w.show()
#displays the widget on the screen. Widgets are first created in memory

#sys.exit(app.exec_())
#we enter the mainloop of the application. 
#The event handling starts from this point. sys.exit() ensures a clean exit