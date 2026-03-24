from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit
from stylesheet import style

def calculate():
    try:
        edit.setText(str(eval(edit.text())))
    except ZeroDivisionError:
        edit.setText("Error: division by zero")
    except Exception:
        edit.setText("Error")


app = QApplication([])
window = QWidget()


##########################
##    Your code here    ##
##########################


window.show()
app.exec()
