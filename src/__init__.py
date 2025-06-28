"""
Anki Card Creator - A tool for creating Anki cards with translations
"""


# Expose main classes at package level for easier imports
from .ui.main_window import MainWindow
from .api.anki_api import AnkiConnect
from .api.translation import TranslationService

__all__ = ['MainWindow', 'AnkiConnect', 'TranslationService']