from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Signal
from api.anki_api import AnkiConnect

class DeckSelector(QComboBox):
    deck_changed = Signal(str)  # Emits deck name when changed
    
    def __init__(self, anki_connect: AnkiConnect, parent=None):
        super().__init__(parent)
        self.anki = anki_connect
        self.setToolTip("Select target deck")
        self.setPlaceholderText("Select deck...")
        
        self.currentTextChanged.connect(self.deck_changed)
        self.refresh_decks()
    
    def refresh_decks(self):
        """Reload decks from Anki"""
        self.clear()
        try:
            decks = self.anki.get_decks()
            if decks:
                self.addItems(decks)
        except Exception as e:
            self.addItem("Error loading decks")
            self.setDisabled(True)
            raise

    @property    
    def current_deck(self) -> str:
        return self.currentText()