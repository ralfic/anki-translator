"""
Anki Card Creator - A tool for creating Anki cards with translations
"""

# Expose main classes at package level for easier imports
from .ui.pages.main_page import MainWindow
from .api.anki_service import AnkiConnect
from .api.translators.googletrans_service import TranslationService

__all__ = ["MainWindow", "AnkiConnect", "TranslationService"]
