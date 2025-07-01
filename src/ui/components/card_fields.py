from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QTextEdit,
)
from PySide6.QtCore import Signal


class CardFields(QWidget):
    translate_requested = Signal()
    add_note_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        # Source field
        self.source_field = QLineEdit()
        self.source_field.setPlaceholderText("Enter text to translate")
        self.source_field.setClearButtonEnabled(True)

        self.source_field.textChanged.connect(
            lambda text: text == "" and self.clear_fields()
        )

        # Translation field
        self.translation_field = QLineEdit()
        self.translation_field.setPlaceholderText("Translation")

        # Extra translations
        self.extra_translations_field = QTextEdit()
        self.extra_translations_field.setPlaceholderText("Extra translations")
        self.extra_translations_field.setReadOnly(True)

        # Buttons
        self.translate_btn = QPushButton("Translate")
        self.add_note_btn = QPushButton("Add to Anki")

        # Status label
        self.status_label = QLabel()
        self.status_label.setStyleSheet("color: gray;")

        self.layout.addWidget(self.source_field)
        self.layout.addWidget(self.translation_field)
        self.layout.addWidget(self.extra_translations_field)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.translate_btn)
        btn_layout.addWidget(self.add_note_btn)
        self.layout.addLayout(btn_layout)

        self.layout.addWidget(self.status_label)

    def setup_connections(self):
        self.translate_btn.clicked.connect(self.translate_requested)
        self.add_note_btn.clicked.connect(self.add_note_requested)
        self.source_field.returnPressed.connect(self.translate_requested)
        self.source_field.textChanged.connect(lambda _: self.set_status(""))

    def set_source_text(self, text: str):
        self.source_field.setText(text)

    def set_translation(self, text: str):
        self.translation_field.setText(text)

    def set_extra_translations(self, text: str):
        self.extra_translations_field.setText(text)

    def clear_fields(self):
        self.source_field.clear()
        self.translation_field.clear()
        self.extra_translations_field.clear()

    def set_status(self, message: str, is_error: bool = False):
        self.status_label.setText(message)
        if is_error:
            self.status_label.setStyleSheet("color: red;")
        else:
            self.status_label.setStyleSheet("color: gray;")

    @property
    def source_text(self):
        return self.source_field.text()

    @property
    def translation(self):
        return self.translation_field.text()

    @property
    def extra_translations(self):
        return self.extra_translations_field.toPlainText()
