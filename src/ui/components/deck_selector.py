from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Signal
from api.anki_service import AnkiService


class DeckSelector(QComboBox):
    deck_changed = Signal(str)

    def __init__(self, anki_service: AnkiService, default_deck: str, parent=None):
        super().__init__(parent)
        self.anki = anki_service
        self.default_deck = default_deck
        self.setToolTip("Select target deck")
        self.setPlaceholderText("Select deck...")

        self.currentTextChanged.connect(self.deck_changed)
        self.refresh_decks()

    def refresh_decks(self):
        self.clear()

        try:
            decks = self.anki.get_decks()
            if decks:
                self.addItems(decks)
        except Exception:
            self.addItem("Error loading decks")
            self.setDisabled(True)

        self.setCurrentText(self.default_deck)

    @property
    def current_deck(self) -> str:
        return self.currentText()
