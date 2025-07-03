import json
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG = {
    "default_source": "EN",
    "default_target": "RU",
    "translators": ["Googletrans", "Deepl translator", "SlovakSk translator"],
    "languages": ["EN", "RU"],
    "default_deck": "Default",
    "default_model": "Basic",
}

CONFIG_PATH = Path("config.json")


class ConfigManager:
    def __init__(self):
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

    def get(self, key: str) -> Any:
        return self.config.get(key)

    def set(self, key: str, value: Any):
        self.config[key] = value
        self._save_config(self.config)
