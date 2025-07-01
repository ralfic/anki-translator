from PySide6.QtWidgets import QComboBox

class TranslatorSelector(QComboBox):
    def __init__(self, translators: list[str]):
        super().__init__()
        self.setup_ui()
        self.addItems(translators)

    def setup_ui(self):
        self.setToolTip("Select translator")

    @property
    def current_translator(self) -> str:
        return self.currentText()
