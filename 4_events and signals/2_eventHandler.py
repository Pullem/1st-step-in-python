import sys
import qdarkstyle
import PyQt5.QtCore
import PyQt5.QtWidgets


class Example(PyQt5.QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def key_press_event(self, e):
        
        if e.key() == PyQt5.QtCore.Qt.Key_Escape:
            self.close()
        
        
if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    ex = Example()
    sys.exit(app.exec_())

'''
we reimplement the key_press_event() event handler.
'''

# if e.key() == Qt.Key_Escape:
#     self.close()
'''
If we click the Escape button, the application terminates.
'''