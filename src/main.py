import sys
from PySide6.QtWidgets import QApplication
from qasync import QEventLoop
import asyncio
from api.anki_service import AnkiService
from api.translators.googletrans_service import GoogleTransService
from api.translators.deepl_service import DeeplService
from api.translators.slovak_sk_service import SlovakSkService
from ui.pages.staked_widget import StackedWidget
from environs import Env
from utils.config_manager import ConfigManager


def main():
    # Initialize application
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    # Load environment variables
    env = Env()
    env.read_env()

    # Initialize services
    anki_service = AnkiService()
    googletrans_service = GoogleTransService()
    deepl_service = DeeplService()
    slovak_sk_service = SlovakSkService()

    # Initialize config
    config = ConfigManager()

    # Initialize window
    window = StackedWidget(
        anki_service, deepl_service, googletrans_service, slovak_sk_service, config
    )
    window.show()

    with loop:
        loop.run_forever()


if __name__ == "__main__":
    main()
