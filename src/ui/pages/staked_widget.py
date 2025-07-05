from PySide6.QtWidgets import (
    QStackedWidget,
    QToolBar,
    QVBoxLayout,
    QWidget,
    QToolButton,
)
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from utils.config_manager import ConfigManager
from utils.styles import APP_STYLESHEET_DARK, APP_STYLESHEET_LIGHT


class StackedWidget(QWidget):
    def __init__(
        self,
        anki_service,
        deepl_service,
        googletrans_service,
        slovak_sk_service,
        config: ConfigManager,
        parent=None,
    ):
        super().__init__(parent)

        self.config = config

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.previous_theme = self.config.get("default_theme")

        # Create toolbar
        self.toolbar = QToolBar("Navigation")
        self.toolbar.setMovable(False)

        # Create stacked widget
        self.stacked_widget = QStackedWidget()

        # Create pages
        self.main_page = MainPage(
            anki_service, deepl_service, googletrans_service, slovak_sk_service, config
        )
        self.settings_page = SettingsPage(config, anki_service)

        config.config_changed.connect(lambda: self.toggle_theme())
        config.config_changed.connect(lambda: self.main_page.setup_default_values())

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.settings_page)

        # Create toolbar buttons
        self.main_action = self.toolbar.addAction("Main")
        self.settings_action = self.toolbar.addAction("Settings")

        # Connect actions to page switching
        self.main_action.triggered.connect(self.show_main_page)
        self.settings_action.triggered.connect(self.show_settings_page)

        # Add widgets to layout
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.stacked_widget)

        # Style and title
        self._set_theme(self.previous_theme)
        self.setWindowTitle("Anki Translator")

        # Set initial page
        self.show_main_page()

    def show_main_page(self):
        self.stacked_widget.setCurrentIndex(0)
        self.highlight_active_button(self.main_action)

    def show_settings_page(self):
        self.stacked_widget.setCurrentIndex(1)
        self.highlight_active_button(self.settings_action)

    def highlight_active_button(self, active_action):
        for action in self.toolbar.actions():
            widget = self.toolbar.widgetForAction(action)
            if isinstance(widget, QToolButton):
                if action == active_action:
                    if self.previous_theme == "dark":
                        widget.setStyleSheet(
                            "background-color: #2b2b2b; border: 1px solid #4a4a4a; border-radius: 4px;"
                        )
                    if self.previous_theme == "light":
                        widget.setStyleSheet(
                            " background-color: #d8e6f7; border: 1px solid #c0d0e0; color: #ffffff "
                        )
                else:
                    widget.setStyleSheet("")

    def toggle_theme(self):
        current_theme = self.config.get("default_theme")
        if current_theme != self.previous_theme:
            self.previous_theme = current_theme
            self._set_theme(current_theme)

    def _set_theme(self, theme):
        match theme:
            case "dark":
                self.setStyleSheet(APP_STYLESHEET_DARK)
            case "light":
                self.setStyleSheet(APP_STYLESHEET_LIGHT)
