from PySide6.QtWidgets import QWidget


class SettingsPage(QWidget):
    def __init__(self, config):
        super().__init__()

        self.setWindowTitle("Settings")
