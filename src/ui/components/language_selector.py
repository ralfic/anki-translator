from PySide6.QtWidgets import QWidget, QHBoxLayout, QComboBox, QPushButton, QSizePolicy
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

        self.setup_ui()
        self.set_default_values(default_source, default_target)
        self.setup_connections()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.from_combo = QComboBox()
        self.from_combo.addItems(self.languages)
        self.from_combo.setToolTip("Select source language")

        self.to_combo = QComboBox()
        self.to_combo.addItems(self.languages)
        self.to_combo.setToolTip("Select target language")

        self.swap_btn = QPushButton("<>")
        self.swap_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.swap_btn.clicked.connect(self.swap_languages)

        layout.addWidget(self.from_combo)
        layout.addWidget(self.swap_btn)
        layout.addWidget(self.to_combo)

        self.setLayout(layout)

    def setup_connections(self):
        self.from_combo.currentTextChanged.connect(self.on_language_changed)
        self.to_combo.currentTextChanged.connect(self.on_language_changed)

    def swap_languages(self):
        prev_from = self.from_combo.currentText()
        prev_to = self.to_combo.currentText()
        self.from_combo.setCurrentText(prev_to)
        self.to_combo.setCurrentText(prev_from)
        self.on_language_changed()

    def set_default_values(self, s_l, t_l):
        self.from_combo.setCurrentText(s_l)
        self.to_combo.setCurrentText(t_l)

    def on_language_changed(self):
        self.language_changed.emit(self.source_language, self.target_language)

    @property
    def source_language(self) -> str:
        return self.from_combo.currentText()

    @property
    def target_language(self) -> str:
        return self.to_combo.currentText()
