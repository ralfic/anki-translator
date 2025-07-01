from googletrans import Translator
from qasync import asyncSlot


class GoogleTransService:
    def __init__(self):
        self.translator = Translator()

    @asyncSlot(str, str, str)
    async def translate(self, text, source_lang, target_lang):
        try:
            result = await self.translator.translate(
                text, src=source_lang, dest=target_lang
            )
            return {
                "text": result.text,
                "pronunciation": result.pronunciation,
                "extra": result.extra_data,
            }
        except Exception as e:
            raise TranslationError(f"Translation failed: {str(e)}")


class TranslationError(Exception):
    pass
