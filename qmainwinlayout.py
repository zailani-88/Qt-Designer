from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QVBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a vertical box layout
        layout = QVBoxLayout()

        # Create buttons
        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")
        btn3 = QPushButton("btn3")
        btn4 = QPushButton("btn4")

        # Add buttons to the layout
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        # Create a central widget and set the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the QMainWindow
        self.setCentralWidget(widget)

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
