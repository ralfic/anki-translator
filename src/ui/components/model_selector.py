from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Signal
from api.anki_api import AnkiConnect

class ModelSelector(QComboBox):
    model_changed = Signal(str)  # Emits model name when changed
    
    def __init__(self, anki_connect: AnkiConnect, parent=None):
        super().__init__(parent)
        self.anki = anki_connect
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
        except Exception as e:
            self.addItem("Error loading models")
            self.setDisabled(True)
            raise

    @property
    def current_model(self) -> str:
        return self.currentText()