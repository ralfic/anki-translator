import json
from pathlib import Path
from typing import Dict, Any, Optional
from typing import overload
from PySide6.QtCore import QObject, Signal

DEFAULT_CONFIG = {
    "default_source": "EN",
    "default_target": "RU",
    "default_theme": "dark",
    "translators": ["Googletrans", "Deepl translator", "SlovakSk translator"],
    "languages": ["EN", "RU"],
    "default_deck": "Default",
    "default_model": "Basic",
}

CONFIG_PATH = Path("config.json")


class ConfigManager(QObject):
    config_changed = Signal()

    def __init__(self):
        super().__init__()
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self._save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

    def _save_config(self, config: Dict[str, Any]):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        self.config_changed.emit()

    @overload
    def get(self) -> Dict[str, Any]: ...

    @overload
    def get(self, key: str) -> Any: ...

    def get(self, key: Optional[str] = None) -> Any:
        if key is None:
            return self.config
        return self.config.get(key)

    def set(self, cnf: Dict):
        for key, value in cnf.items():
            self.config[key] = value
        self._save_config(self.config)
