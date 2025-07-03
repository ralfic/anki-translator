APP_STYLESHEET = """
QWidget {
    background-color: #2b2b2b;
    color: #ffffff;
    font-family: Segoe UI, sans-serif;
    font-size: 13px;
}

/* QToolBar Styling */
QToolBar {
    background-color: #3c3f41;
    border-bottom: 1px solid #444;
    spacing: 6px;
    padding: 4px;
}

QToolButton {
    background-color: transparent;
    color: #ffffff;
    padding: 2px 4px;
    border: none;
}

QToolButton:hover {
    background-color: #505050;
    border-radius: 4px;
}

QToolButton:checked {
    background-color: #2b2b2b;
    border: 1px solid #888;
    border-radius: 4px;
}

QLineEdit, QTextEdit {
    background-color: #3c3f41;
    color: #ffffff;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 4px;
}

QComboBox QAbstractItemView {
    background-color: #3c3f41;
    selection-background-color: #5588ff;
    color: #ffffff;
}

QComboBox {
    background-color: #3c3f41; /* Light: #ffffff */
    color: #ffffff;            /* Light: #000000 */
    border: 1px solid #555;    /* Light: #aaa */
    border-radius: 4px;
    padding: 4px;
    padding-right: 20px; /* Space for arrow */
}

QComboBox:hover {
    border: 1px solid #888;    /* Light: #888 */
}

QComboBox:focus {
    border: 1px solid #5588ff;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 18px;
    border-left: 1px solid #555; /* Light: #aaa */
    background-color: #444;      /* Light: #e0e0e0 */
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
}

QComboBox::down-arrow {
    width: 12px;
    height: 12px;
}

QPushButton {
    background-color: #444;
    border: 1px solid #666;
    border-radius: 4px;
    padding: 6px;
    color: #ffffff;
}

QPushButton:hover {
    background-color: #555;
}

QPushButton:pressed {
    background-color: #333;
}

QTabWidget::pane {
    border: 1px solid #444;
}

QTabBar::tab {
    background: #3c3f41;
    color: #fff;
    padding: 6px;
    border: 1px solid #444;
    border-bottom: none;
    border-radius: 4px 4px 0 0;
}

QTabBar::tab:selected {
    background: #2b2b2b;
    font-weight: bold;
}
"""
