from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from my_login import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Login form")
        self.icon = "image.png"
        self.setWindowIcon(QIcon(self.icon))
        
    
app = QApplication()
window = MainWindow()
window.show()
app.exec()