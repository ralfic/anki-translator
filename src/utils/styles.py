APP_STYLESHEET_DARK = """
QWidget {
    background-color: #2b2b2b;
    color: #e0e0e0;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
    selection-background-color: #3d6e99;
    selection-color: #ffffff;
}

/* Main Window and Background Elements */
QMainWindow {
    background-color: #252525;
    border: 1px solid #1a1a1a;
}

/* Toolbar Styling */
QToolBar {
    background-color: #353535;
    border-bottom: 1px solid #2a2a2a;
    spacing: 6px;
    padding: 4px;
}

QToolButton {
    background-color: transparent;
    color: #e0e0e0;
    padding: 4px 6px;
    border: none;
    border-radius: 4px;
}

QToolButton:hover {
    background-color: #4a4a4a;
}

QToolButton:pressed {
    background-color: #3a3a3a;
}

QToolButton:checked {
    background-color: #2d2d2d;
    border: 1px solid #4a4a4a;
}

/* Input Fields */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #333333;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 5px 8px;
    selection-background-color: #3d6e99;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #4a7bac;
}

/* ComboBox Styling */
QComboBox {
    background-color: #333333;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 5px 8px;
    padding-right: 25px;
    min-width: 6em;
}

QComboBox:hover {
    border: 1px solid #4a4a4a;
}

QComboBox:focus {
    border: 1px solid #4a7bac;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #3a3a3a;
    background-color: #3a3a3a;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    width: 12px;
    height: 12px;
}

QComboBox QAbstractItemView {
    background-color: #333333;
    border: 1px solid #3a3a3a;
    selection-background-color: #3d6e99;
    selection-color: #ffffff;
    outline: none;
}

/* Buttons */
QPushButton {
    background-color: #3a3a3a;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 6px 12px;
    min-width: 80px;
}

QPushButton:hover {
    background-color: #4a4a4a;
    border: 1px solid #4a4a4a;
}

QPushButton:pressed {
    background-color: #2d2d2d;
    border: 1px solid #2d2d2d;
}

QPushButton:disabled {
    background-color: #2d2d2d;
    color: #6a6a6a;
    border: 1px solid #2d2d2d;
}

/* Tab Widgets */
QTabWidget::pane {
    border: 1px solid #3a3a3a;
    top: -1px;
}

QTabBar::tab {
    background: #353535;
    color: #b0b0b0;
    padding: 6px 12px;
    border: 1px solid #3a3a3a;
    border-bottom: none;
    border-radius: 4px 4px 0 0;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background: #2b2b2b;
    color: #e0e0e0;
    border-bottom: 1px solid #2b2b2b;
    margin-bottom: -1px;
}

QTabBar::tab:hover {
    background: #3a3a3a;
}

/* Scrollbars */
QScrollBar:vertical {
    border: none;
    background: #333333;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #4a4a4a;
    min-height: 20px;
    border-radius: 4px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

/* Status Bar */
QStatusBar {
    background-color: #353535;
    color: #b0b0b0;
    border-top: 1px solid #2a2a2a;
}

/* Menu Bar */
QMenuBar {
    background-color: #353535;
    color: #e0e0e0;
    border-bottom: 1px solid #2a2a2a;
}

QMenuBar::item {
    padding: 4px 8px;
    background: transparent;
}

QMenuBar::item:selected {
    background: #4a4a4a;
}

QMenu {
    background-color: #353535;
    border: 1px solid #3a3a3a;
    padding: 4px;
}

QMenu::item {
    padding: 4px 24px 4px 8px;
}

QMenu::item:selected {
    background-color: #4a4a4a;
}

QMenu::separator {
    height: 1px;
    background: #3a3a3a;
    margin: 4px 0;
}
"""

APP_STYLESHEET_LIGHT = """
QWidget {
    background-color: #f5f5f5;
    color: #333333;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
    selection-background-color: #4a90e2;
    selection-color: #ffffff;
}

/* Main Window and Background Elements */
QMainWindow {
    background-color: #ffffff;
    border: 1px solid #dddddd;
}

/* Toolbar Styling */
QToolBar {
    background-color: #f0f0f0;
    border-bottom: 1px solid #e0e0e0;
    spacing: 6px;
    padding: 4px;
}

QToolButton {
    background-color: transparent;
    color: #444444;
    padding: 4px 6px;
    border: none;
    border-radius: 4px;
}

QToolButton:hover {
    background-color: #e5e5e5;
}

QToolButton:pressed {
    background-color: #d5d5d5;
    color: #ffffff
}

QToolButton:checked {
    background-color: #d8e6f7;
    border: 1px solid #c0d0e0;
    color: #ffffff

}

/* Input Fields */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #ffffff;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 5px 8px;
    selection-background-color: #4a90e2;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #4a90e2;
    background-color: #f8f8f8;
}

/* ComboBox Styling */
QComboBox {
    background-color: #ffffff;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 5px 8px;
    padding-right: 25px;
    min-width: 6em;
}

QComboBox:hover {
    border: 1px solid #aaaaaa;
}

QComboBox:focus {
    border: 1px solid #4a90e2;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #dddddd;
    background-color: #f0f0f0;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    width: 12px;
    height: 12px;
}

QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    selection-background-color: #4a90e2;
    selection-color: #ffffff;
    outline: none;
}

/* Buttons */
QPushButton {
    background-color: #f0f0f0;
    color: #333333;
    border: 1px solid #cccccc;
    border-radius: 4px;
    padding: 6px 12px;
    min-width: 80px;
}

QPushButton:hover {
    background-color: #e5e5e5;
    border: 1px solid #bbbbbb;
}

QPushButton:pressed {
    background-color: #d5d5d5;
    border: 1px solid #aaaaaa;
}

QPushButton:disabled {
    background-color: #f5f5f5;
    color: #aaaaaa;
    border: 1px solid #e0e0e0;
}

/* Tab Widgets */
QTabWidget::pane {
    border: 1px solid #dddddd;
    top: -1px;
}

QTabBar::tab {
    background: #f0f0f0;
    color: #666666;
    padding: 6px 12px;
    border: 1px solid #dddddd;
    border-bottom: none;
    border-radius: 4px 4px 0 0;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background: #ffffff;
    color: #333333;
    border-bottom: 1px solid #ffffff;
    margin-bottom: -1px;
}

QTabBar::tab:hover {
    background: #e8e8e8;
}

/* Scrollbars */
QScrollBar:vertical {
    border: none;
    background: #f0f0f0;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #d0d0d0;
    min-height: 20px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background: #c0c0c0;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    background: none;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

/* Status Bar */
QStatusBar {
    background-color: #f0f0f0;
    color: #666666;
    border-top: 1px solid #e0e0e0;
}

/* Menu Bar */
QMenuBar {
    background-color: #f0f0f0;
    color: #444444;
    border-bottom: 1px solid #e0e0e0;
}

QMenuBar::item {
    padding: 4px 8px;
    background: transparent;
}

QMenuBar::item:selected {
    background: #e5e5e5;
}

QMenu {
    background-color: #ffffff;
    border: 1px solid #dddddd;
    padding: 4px;
}

QMenu::item {
    padding: 4px 24px 4px 8px;
}

QMenu::item:selected {
    background-color: #e8f0fe;
    color: #1a73e8;
}

QMenu::separator {
    height: 1px;
    background: #eeeeee;
    margin: 4px 0;
}

/* Special Elements */
QProgressBar {
    border: 1px solid #cccccc;
    border-radius: 4px;
    background-color: #ffffff;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #4a90e2;
    width: 10px;
}
"""
