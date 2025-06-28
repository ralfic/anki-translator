from PySide6.QtWidgets import QWidget, QHBoxLayout, QComboBox
from PySide6.QtCore import Signal

MY_LANGUAGES = ["sk", "ru","en"]
DEFAULT_TARGET_LANGUAGE = "en"
DEFAULT_SOURCE_LANGUAGE = "sk"


class LanguageSelector(QWidget):
    language_changed = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QHBoxLayout(self)
        
        self.from_combo = QComboBox()
        self.from_combo.addItems(MY_LANGUAGES)  
        self.from_combo.setToolTip("Select source language")

        self.to_combo = QComboBox()
        self.to_combo.addItems(MY_LANGUAGES)
        self.to_combo.setToolTip("Select target language")

        self.layout.addWidget(self.from_combo)
        self.layout.addWidget(self.to_combo)


        self.refresh_languages()

    def refresh_languages(self):
        self.from_combo.clear()
        self.to_combo.clear()

        self.from_combo.addItems(MY_LANGUAGES)
        self.to_combo.addItems(MY_LANGUAGES) 

        self.from_combo.setCurrentText(DEFAULT_SOURCE_LANGUAGE)
        self.to_combo.setCurrentText(DEFAULT_TARGET_LANGUAGE)
    
    def setup_connections(self):
        self.from_combo.currentTextChanged.connect(self.on_language_changed)
        self.to_combo.currentTextChanged.connect(self.on_language_changed)
    
    def on_language_changed(self):
        self.language_changed.emit(self.source_language, self.target_language)

    
    @property
    def source_language(self):
        return self.from_combo.currentText()
    
    @property
    def target_language(self):
        return self.to_combo.currentText()

     

  