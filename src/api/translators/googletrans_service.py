from googletrans import Translator
from qasync import asyncSlot


class GoogleTransService:
    def __init__(self):
        self.translator = Translator()

    @asyncSlot(str, str, str)
    async def translate(self, text: str, source_lang: str, target_lang: str):
        try:
            resp = await self.translator.translate(
                text, src=source_lang, dest=target_lang
            )

            return {
                "text": resp.text,
                "pronunciation": resp.pronunciation,
                "extra": resp.extra_data,
            }

        except Exception as e:
            raise TranslationError(f"Translation failed: {str(e)}")


class TranslationError(Exception):
    pass
