import sys
import qdarkstyle
import PyQt5.QtCore
import PyQt5.QtWidgets


class Example(PyQt5.QtWidgets.QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.init_ui()

	def init_ui(self):
		
		lcd = PyQt5.QtWidgets.QLCDNumber(self)  # https://doc.qt.io/qt-5/qlcdnumber.html#details
		sld = PyQt5.QtWidgets.QSlider(PyQt5.QtCore.Qt.Horizontal, self)

		vbox = PyQt5.QtWidgets.QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display)
		
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Signal & slot')
		self.show()
		

if __name__ == '__main__':
	
	app = PyQt5.QtWidgets.QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

	ex = Example()
	sys.exit(app.exec_())

'''
we display a QtGui.QLCDNumber and a QtGui.QSlider. 
We change the lcd number by dragging the slider knob.
'''

# sld.valueChanged.connect(lcd.display)
'''
Here we connect a valueChanged signal of the slider to 
the display slot of the lcd number.

The sender is an object that sends a signal. 
The receiver is the object that receives the signal. 
The slot is the method that reacts to the signal.
'''