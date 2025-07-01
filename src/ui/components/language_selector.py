from PySide6.QtWidgets import QWidget, QHBoxLayout, QComboBox
from PySide6.QtCore import Signal


class LanguageSelector(QWidget):
    language_changed = Signal(str, str)

    def __init__(
        self,
        languages: list[str],
        default_source: str,
        default_target: str,
        parent=None,
    ):
        super().__init__(parent)
        self.languages = languages
        self.default_source = default_source
        self.default_target = default_target

        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(8, 0, 8, 0)

        self.from_combo = QComboBox()
        self.from_combo.addItems(self.languages)
        self.from_combo.setToolTip("Select source language")
        self.from_combo.setCurrentText(self.default_source)

        self.to_combo = QComboBox()
        self.to_combo.addItems(self.languages)
        self.to_combo.setToolTip("Select target language")
        self.to_combo.setCurrentText(self.default_target)

        self.layout.addWidget(self.from_combo)
        self.layout.addWidget(self.to_combo)

    def setup_connections(self):
        self.from_combo.currentTextChanged.connect(self.on_language_changed)
        self.to_combo.currentTextChanged.connect(self.on_language_changed)

    def on_language_changed(self):
        self.language_changed.emit(self.source_language, self.target_language)

    @property
    def source_language(self) -> str:
        return self.from_combo.currentText()

    @property
    def target_language(self) -> str:
        return self.to_combo.currentText()
