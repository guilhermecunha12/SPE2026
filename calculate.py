def calculate(edit):
    try:
        edit.setText(str(eval(edit.text())))
    except ZeroDivisionError:
        edit.setText("Error: division by zero")
    except Exception:
        edit.setText("Error")
