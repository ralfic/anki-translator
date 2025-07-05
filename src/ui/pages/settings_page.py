from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QPushButton,
    QSizePolicy,
    QHBoxLayout,
    QRadioButton,
)
from PySide6.QtCore import Signal
from ui.components import (
    DeckSelector,
    ModelSelector,
    LanguageSelector,
)
from utils.config_manager import ConfigManager


class SettingsPage(QWidget):
    settings_changed = Signal()

    def __init__(self, config: ConfigManager, anlki_service):
        super().__init__()
        # Config
        self.config = config
        self.current_theme = self.config.get("default_theme")

        # Services
        self.anki_service = anlki_service

        # UI | Connections
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        # Main page
        self.setWindowTitle("Settings")

        # Main layout
        main_layout = QVBoxLayout()

        # Add components
        self.deck_selector = DeckSelector(
            self.anki_service, default_deck=self.config.get("default_deck")
        )
        self.model_selector = ModelSelector(
            self.anki_service, default_model=self.config.get("default_model")
        )

        self.radio_btn_dark_theme = QRadioButton("Dark", self)
        self.radio_btn_light_theme = QRadioButton("Light", self)

        match self.current_theme:
            case "dark":
                self.radio_btn_dark_theme.setChecked(True)
            case "light":
                self.radio_btn_light_theme.setChecked(True)
            case _:
                pass

        self.language_selector = LanguageSelector(
            languages=self.config.get("languages"),
            default_source=self.config.get("default_source"),
            default_target=self.config.get("default_target"),
        )
        self.language_selector.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.save_btn = QPushButton("Save")

        theme_layout = QHBoxLayout()
        theme_layout.addWidget(self.radio_btn_dark_theme)
        theme_layout.addWidget(self.radio_btn_light_theme)

        options_layout = QVBoxLayout()
        options_layout.addWidget(self.deck_selector)
        options_layout.addWidget(self.model_selector)
        options_layout.addLayout(theme_layout)
        options_layout.addWidget(self.language_selector)

        main_layout.addLayout(options_layout)
        main_layout.addWidget(self.save_btn)

        self.setLayout(main_layout)

    def setup_connections(self):
        self.save_btn.clicked.connect(self.save_settings)
        self.save_btn.clicked.connect(self.settings_changed)
        self.radio_btn_dark_theme.toggled.connect(self.on_toggle_theme)
        self.radio_btn_light_theme.toggled.connect(self.on_toggle_theme)

    def save_settings(self):
        values_saving = {
            "default_deck": self.deck_selector.current_deck,
            "default_model": self.model_selector.current_model,
            "default_source": self.language_selector.source_language,
            "default_target": self.language_selector.target_language,
            "default_theme": self.current_theme,
        }
        self.config.set(values_saving)

    def on_toggle_theme(self):
        if self.radio_btn_dark_theme.isChecked():
            self.current_theme = "dark"
        if self.radio_btn_light_theme.isChecked():
            self.current_theme = "light"
