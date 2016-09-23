import sys
import qdarkstyle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()
        
        
    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            self.close()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    ex = Example()
    sys.exit(app.exec_())

'''
we reimplement the keyPressEvent() event handler.
'''

# if e.key() == Qt.Key_Escape:
#     self.close()
'''
If we click the Escape button, the application terminates.
'''