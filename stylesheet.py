def style(window):
    window.setStyleSheet("""
    /* ── Main window ── */
    QWidget {
        background-color: #1c1c1e;
        color: #ffffff;
        font-family: 'Segoe UI', 'SF Pro Display', sans-serif;
    }

    /* ── Display ── */
    QLineEdit {
        background-color: #2c2c2e;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 8px 14px;
        font-size: 22pt;
        font-weight: 300;
    }

    /* ── All buttons base style ── */
    QPushButton {
        min-height: 52px;
        min-width:  52px;
        font-size: 16pt;
        font-weight: 500;
        border-radius: 10px;
        border: none;
        background-color: #3a3a3c;
        color: #ffffff;
        margin: 2px;
    }
    QPushButton:hover {
        background-color: #48484a;
    }
    QPushButton:pressed {
        background-color: #636366;
    }

    /* ── Operator buttons  (+, -, *, /) ── */
    QPushButton[text="+"],
    QPushButton[text="-"],
    QPushButton[text="*"],
    QPushButton[text="/"] {
        background-color: #ff9f0a;
        color: #ffffff;
    }
    QPushButton[text="+"]:hover,
    QPushButton[text="-"]:hover,
    QPushButton[text="*"]:hover,
    QPushButton[text="/"]:hover {
        background-color: #ffb340;
    }
    QPushButton[text="+"]:pressed,
    QPushButton[text="-"]:pressed,
    QPushButton[text="*"]:pressed,
    QPushButton[text="/"]:pressed {
        background-color: #cc7f08;
    }

    /* ── Equals button ── */
    QPushButton[text="="] {
        background-color: #30d158;
        color: #ffffff;
    }
    QPushButton[text="="]:hover  { background-color: #34e35f; }
    QPushButton[text="="]:pressed { background-color: #25a645; }

    /* ── Clear button ── */
    QPushButton[text="C"] {
        background-color: #ff453a;
        color: #ffffff;
    }
    QPushButton[text="C"]:hover  { background-color: #ff6961; }
    QPushButton[text="C"]:pressed { background-color: #cc372e; }
    """)
