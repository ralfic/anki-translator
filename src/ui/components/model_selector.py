from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Signal
from api.anki_service import AnkiService


class ModelSelector(QComboBox):
    model_changed = Signal(str)

    def __init__(self, anki_service: AnkiService, default_model: str, parent=None):
        super().__init__(parent)
        self.anki = anki_service
        self.default_model = default_model
        self.setToolTip("Select note type")
        self.setPlaceholderText("Select model...")

        self.currentTextChanged.connect(self.model_changed)
        self.refresh_models()

    def refresh_models(self):
        self.clear()
        try:
            models = self.anki.get_models()
            if models:
                self.addItems(models)
        except Exception:
            self.setPlaceholderText("Error loading models")
            self.setDisabled(True)

        self.setCurrentText(self.default_model)

    @property
    def current_model(self) -> str:
        return self.currentText()
