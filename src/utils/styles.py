APP_STYLESHEET = """
* { font-size: 14px; font-family: Arial, sans-serif; } 
QHBoxLayout {padding: 0px; margin: 0px}

QHBoxLayout {padding: 0px; margin: 0px}

QLineEdit { 
            background-color: #f0f0f0;
            color: black; 
            padding: 5px 3px; 
            border: 1px solid #ccc; 
            border-radius: 4px;
        } 
QPushButton { 
            color: white; 
            padding: 4px 2px 4px 2px;
             } 
QComboBox {  
            padding: 5px 3px; 
        }
QLabel { 
            padding: 5px 3px; 
        }
QTextEdit { 
            background-color: #f0f0f0;
            color: black; 
            padding: 5px 3px; 
            border: 1px solid #ccc; 
            border-radius: 4px;
        }

QToolBar {
    background-color: #2d2d2d;
    border: none;
    border-bottom: 1px solid #1e1e1e;
    padding: 2x;
    spacing: 2px;
}

/* ToolButton styling */
QToolButton {
    background-color: transparent;
    border: 1px solid transparent;
    border-radius: 4px;
    padding: 2px 4x;
    margin: 2px;
    color: #e0e0e0;
}

/* Button states */
QToolButton:hover {
    background-color: #ba4479;
    border: 1px solid #4d4d4d;
}

QToolButton:checked {
    color: black;
    background: #ba4479;
    border: 1px solid #4d4d4d;
}

QToolButton: {
    background: #ba4479;
    border: 1px solid #4d4d4d;
    
}

/* Active button highlight */


/* Separator styling */
QToolBar::separator {
    background-color: #ba4479;
    width: 1px;
    margin: 4px 6px;
}

/* Dropdown arrow styling */
QToolButton::menu-indicator {
    image: none;
    width: 0;
}

/* Icon-only buttons */
QToolButton[popupMode="1"] {
    padding-right: 6px;
}

/* Disabled buttons */
QToolButton:disabled {
    color: #606060;
}
"""
