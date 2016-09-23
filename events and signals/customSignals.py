import sys
import qdarkstyle
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
	
	closeApp = pyqtSignal() 
	

class Example(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      

		self.c = Communicate()
		self.c.closeApp.connect(self.close)       
		
		self.setGeometry(300, 300, 290, 150)
		self.setWindowTitle('Emit signal')
		self.show()
		
		
	def mousePressEvent(self, event):
		
		self.c.closeApp.emit()
		
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
We create a new signal called 'closeApp'. 
This signal is emitted during a mouse press event. 
The signal is connected to the close() slot of the QMainWindow.
'''

# class Communicate(QObject):
#     closeApp = pyqtSignal()
''' 
A signal is created with the pyqtSignal() as 
a class attribute of the external Communicate class.
'''

# self.c = Communicate()
# self.c.closeApp.connect(self.close) 
''' 
The custom closeApp signal is connected to the close() slot of the QMainWindow.
'''

# def mousePressEvent(self, event):
    # self.c.closeApp.emit()
'''
When we click on the window with a mouse pointer, 
the closeApp signal is emitted. The application terminates.
'''