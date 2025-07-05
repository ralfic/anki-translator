from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Signal
from api.anki_service import AnkiService


class ModelSelector(QComboBox):
    model_changed = Signal(str)

    def __init__(self, anki_service: AnkiService, default_model: str, parent=None):
        super().__init__(parent)
        self.anki = anki_service
        self.setToolTip("Select note type")
        self.setPlaceholderText("Select model...")

        self.currentTextChanged.connect(self.model_changed)
        self.get_models()
        self.set_default_values(default_model)

    def get_models(self):
        self.clear()
        try:
            models = self.anki.get_models()
            if models:
                self.addItems(models)
        except Exception:
            self.setPlaceholderText("Error loading models")
            self.setDisabled(True)

    def set_default_values(self, module):
        self.setCurrentText(module)

    @property
    def current_model(self) -> str:
        return self.currentText()
