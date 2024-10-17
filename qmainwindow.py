# =============== Menggunakan QMainWindow =======================
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()

# cara 1
#label = QLabel("Label", window) 
# cara 2
label = QLabel(window)  
label.setText("Label1")
label.move(200, 0)

# cara 1
#button = QPushButton("MyButton", window)
# cara 2
button = QPushButton(window)
button.setText("Button1")

window.show()
app.exec_()
