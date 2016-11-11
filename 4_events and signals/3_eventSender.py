import sys

import PyQt5.QtWidgets

import qdarkstyle
import PyQt5.QtWidgets


class Example(PyQt5.QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def init_ui(self):

        btn1 = PyQt5.QtWidgets.QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = PyQt5.QtWidgets.QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def button_clicked(self):
      
        sender = self.sender()
        print("This is the 'sender' :", sender)
        print("This is 'sender.text' :", sender.text)
        print("And this is the content / value of 'sender.text' :", sender.text())
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    ex = Example()
    sys.exit(app.exec_())

'''
In the button_clicked() method we determine which button
we have clicked by calling the sender() method.
'''

# btn1.clicked.connect(self.button_clicked)
# btn2.clicked.connect(self.button_clicked)
''' Both buttons are connected to the same slot. '''


# def button_clicked(self):
#     sender = self.sender()
#     self.statusBar().showMessage(sender.text() + ' was pressed')
'''
We determine the signal source by calling the sender() method. 
In the statusbar of the application, we show the label of the button 
being pressed.
'''