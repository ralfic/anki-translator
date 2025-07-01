from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import QThread
from ui.components import (
    DeckSelector,
    ModelSelector,
    LanguageSelector,
    CardFields,
    TranslatorSelector,
)
from utils.config_manager import ConfigManager
from utils.clipboard import ClipboardMonitor
from qasync import asyncSlot


class MainPage(QMainWindow):
    def __init__(
        self, anlki_service, deepl_service, googletrans_service, config: ConfigManager
    ):
        super().__init__()
        # Services
        self.anki_service = anlki_service
        self.googletrans_service = googletrans_service
        self.deepl_service = deepl_service

        # Config
        self.config = config

        # UI | Connections
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        # Main page
        self.setWindowTitle("Anki translator")

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Add components
        self.deck_selector = DeckSelector(
            self.anki_service, default_deck=self.config.get("default_deck")
        )
        self.model_selector = ModelSelector(
            self.anki_service, default_model=self.config.get("default_model")
        )
        self.translator_selector = TranslatorSelector(
            translators=self.config.get("translators")
        )
        self.language_selector = LanguageSelector(
            languages=self.config.get("languages"),
            default_source=self.config.get("default_source"),
            default_target=self.config.get("default_target"),
        )
        self.card_fields = CardFields()

        comb_layout = QVBoxLayout()
        comb_layout.addWidget(self.deck_selector)
        comb_layout.addWidget(self.model_selector)
        comb_layout.addWidget(self.translator_selector)
        comb_widget = QWidget()
        comb_widget.setLayout(comb_layout)

        main_layout.addWidget(comb_widget)
        main_layout.addWidget(self.language_selector)
        main_layout.addWidget(self.card_fields)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Add clipboard monitor
        self.clipboard_monitor = ClipboardMonitor()
        self.clipboard_monitor.text_changed.connect(self.card_fields.set_source_text)

        # Start clipboard monitor
        self.thread = QThread()
        self.clipboard_monitor.moveToThread(self.thread)
        self.thread.started.connect(self.clipboard_monitor.start_listening)
        self.thread.start()

    def setup_connections(self):
        self.card_fields.translate_requested.connect(self.on_translate_requested)
        self.card_fields.add_note_requested.connect(self.on_add_note_requested)

    @asyncSlot()
    async def on_translate_requested(self):
        source_text = self.card_fields.source_text
        source_lang = self.language_selector.source_language
        target_lang = self.language_selector.target_language
        current_translator = self.translator_selector.current_translator

        if source_text:
            try:
                if current_translator == "Googletrans":
                    translation = await self.googletrans_service.translate(
                        source_text, source_lang, target_lang
                    )
                    if translation:
                        extra_translations = translation.get("extra").get(
                            "all-translations"
                        )[0][1]
                        self.card_fields.set_translation(translation.get("text"))
                        if extra_translations:
                            self.card_fields.set_extra_translations(
                                "\n".join(extra_translations)
                            )
                elif current_translator == "Deepl translator":
                    translation = self.deepl_service.translate(
                        source_text, source_lang, target_lang
                    )
                    if translation:
                        self.card_fields.set_translation(translation.get("text"))

            except Exception as e:
                self.card_fields.set_status(f"Translation failed: {str(e)}", True)
                return

    def on_add_note_requested(self):
        source_text = self.card_fields.source_text
        translation = self.card_fields.translation
        deck = self.deck_selector.current_deck
        model = self.model_selector.current_model
        try:
            self.anki_service.add_note(
                deck_name=deck,
                model_name=model,
                fields={"Front": source_text, "Back": translation},
            )
            self.card_fields.set_status("Note added successfully", False)
        except Exception as e:
            self.card_fields.set_status(f"Adding note failed: {str(e)}", True)
