from PySide6.QtWidgets import (
    QStackedWidget,
    QToolBar,
    QVBoxLayout,
    QWidget,
    QToolButton,
)
from PySide6.QtCore import Qt
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from utils.styles import APP_STYLESHEET
from utils.config_manager import ConfigManager


class StackedWidget(QWidget):
    def __init__(
        self,
        anlki_service,
        deepl_service,
        googletrans_service,
        config: ConfigManager,
        parent=None,
    ):
        super().__init__(parent)

        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create toolbar
        self.toolbar = QToolBar("Navigation")
        self.toolbar.setMovable(False)

        # Create stacked widget
        self.stacked_widget = QStackedWidget()

        # Create pages
        self.main_page = MainPage(
            anlki_service, deepl_service, googletrans_service, config
        )
        self.settings_page = SettingsPage(config)

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
        self.setStyleSheet(APP_STYLESHEET)
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
        """Visual feedback for active tab"""
        for action in self.toolbar.actions():
            widget = self.toolbar.widgetForAction(action)
            if isinstance(widget, QToolButton):
                if action == active_action:
                    widget.setStyleSheet("background-color: #ba4479;")
                else:
                    widget.setStyleSheet("")
