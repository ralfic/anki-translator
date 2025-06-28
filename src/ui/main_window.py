from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import QThread
from ui.components import DeckSelector, ModelSelector, LanguageSelector, CardFields
from utils.clipboard import ClipboardMonitor
from utils.styles import APP_STYLESHEET
from qasync import asyncSlot 


class MainWindow(QMainWindow):
    def __init__(self, anki_connect, translation_service):  
        super().__init__()
        self.anki = anki_connect
        self.translator = translation_service
        
        self.setup_ui()
        self.setup_connections()
        
    def setup_ui(self):
        #Main window
        self.setWindowTitle("Anki adding cards")
        self.setMaximumSize(500, 400)
        self.setStyleSheet(APP_STYLESHEET)

        #Main layout
        main_layout = QVBoxLayout()

        #Add components
        self.deck_selector = DeckSelector(self.anki)
        self.model_selector = ModelSelector(self.anki)
        self.language_selector = LanguageSelector()
        self.card_fields = CardFields()
        
        main_layout.addWidget(self.deck_selector)
        main_layout.addWidget(self.model_selector)
        main_layout.addWidget(self.language_selector)
        main_layout.addWidget(self.card_fields)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

         #Add clipboard monitor
        self.clipboard_monitor = ClipboardMonitor()
        self.clipboard_monitor.text_changed.connect(self.card_fields.set_source_text)
        
        #Start clipboard monitor
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

        if source_text:
            try: 
                translation = await self.translator.translate(source_text, source_lang, target_lang)
                extra_translations = translation.get('extra').get("all-translations")[0][1]
                self.card_fields.set_translation(translation.get('text'))
                if extra_translations:
                    self.card_fields.set_extra_translations("\n".join(extra_translations))
            except Exception as e:
                self.card_fields.set_status(f"Translation failed: {str(e)}", True)
                return
            

    def on_add_note_requested(self):
        source_text = self.card_fields.source_text
        translation = self.card_fields.translation
        deck = self.deck_selector.current_deck
        model = self.model_selector.current_model
        try:
            self.anki.add_note(deck_name=deck, model_name=model, fields={"Front": source_text, "Back": translation})
            self.card_fields.set_status("Note added successfully", False)
        except Exception as e:
            self.card_fields.set_status(f"Adding note failed: {str(e)}", True) 
