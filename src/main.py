import sys
from PySide6.QtWidgets import QApplication
from qasync import QEventLoop
import asyncio
from ui.main_window import MainWindow
from api.anki_api import AnkiConnect
from api.translation import TranslationService

def main():
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    
    # Initialize services
    anki_connect = AnkiConnect()
    translation_service = TranslationService()
    
    window = MainWindow(anki_connect, translation_service)
    window.show()
    
    with loop:
        loop.run_forever()
 
if __name__ == "__main__":
    main()
    