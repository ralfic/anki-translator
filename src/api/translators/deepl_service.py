import deepl
from environs import Env
from typing import Optional


class DeeplService:
    def __init__(self, env: Optional[Env] = None):
        self.env = env or Env()
        self.api_key = self.env.str("DEEPL_API_KEY", default="")
        self.translator = deepl.Translator(self.api_key)

    def _is_en(self, lang: str) -> str:
        return "EN-US" if lang == "EN" else lang

    def translate(self, text: str, source_lang: str, target_lang: str):
        try:
            resp = self.translator.translate_text(
                text=text,
                source_lang=source_lang,
                target_lang=self._is_en(target_lang),
            )

            return {
                "text": resp.text,
            }
        except Exception as e:
            raise TranslationError(f"Translation failed: {str(e)}")


class TranslationError(Exception):
    pass
