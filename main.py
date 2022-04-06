from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, \
    QComboBox, QLabel
from PyQt6.QtGui import QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 ComboBox")
        self.setGeometry(500,200, 500,400)

        vbox = QVBoxLayout()

        self.combo = QComboBox()

        self.combo.addItem("PyQt6")
        self.combo.addItem("Wx")
        self.combo.addItem("Kivy")
        self.combo.addItem("Tkinter")
        self.combo.addItem("Remi")

        self.combo.currentTextChanged.connect(self.item_selected)

        self.label = QLabel("")
        self.label.setFont(QFont("Times New Roman", 15))
        self.label.setStyleSheet('color:brown')

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_selected(self):
        item = self.combo.currentText()
        self.label.setText("You have selected : " + item)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())