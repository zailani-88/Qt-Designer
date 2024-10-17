from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # Creating buttons and adding them to the layout
        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")
        btn3 = QPushButton("btn3")
        btn4 = QPushButton("btn4")

        # Adding buttons to the layout
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        # Set the layout for the window
        self.setLayout(layout)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
