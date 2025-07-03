import requests
from bs4 import BeautifulSoup
from typing import Optional, Dict, List
from enum import Enum
import logging

logger = logging.getLogger(__name__)

BASE_SLOVAK_SK_URL = "https://slovnik.aktuality.sk/preklad"

# Possible languages: SK-EN, EN-SK, RU-SK, SK-RU
class LanguagePair(Enum):
    SK_EN = "slovensko-anglicky"
    EN_SK = "anglicko-slovensky"
    RU_SK = "rusko-slovensky"
    SK_RU = "slovensko-rusky"

    @classmethod
    def get_pair(cls, source: str, target: str) -> "LanguagePair":
        try:
            return cls[f"{source}_{target}"]
        except KeyError:
            raise ValueError(f"Unsupported language pair: {source}-{target}")


class SlovakSkService:
    def __init__(self):
        pass

    def translate(
        self, text: str, source_lang: str, target_lang: str
    ) -> Optional[Dict[str, List[str]]]:

        try:
            if not text.strip():
                return None

            lang_pair = LanguagePair.get_pair(source_lang, target_lang)

            url = f"{BASE_SLOVAK_SK_URL}/{lang_pair.value}/?q={text}"

            resp = requests.get(url)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.content, "html.parser")
            res = {}

            for li in soup.find_all("li", class_="leading-7 list-item"):
                translation = BeautifulSoup(str(li), "html.parser")
                slovak = translation.find(
                    "a", href=lambda x: x and "/preklad/slovensko-rusky" in x
                )
                slovak_text = slovak.get_text(strip=True, separator=" ")
                russian = translation.find(
                    "a", href=lambda x: x and "/preklad/rusko-slovensky" in x
                )
                russian_text = russian.get_text(strip=True)
                if slovak_text in res.keys():
                    res[slovak_text].append(russian_text)
                else:
                    res[slovak_text] = [russian_text]

            return res if res else None

        except requests.RequestException as e:
            logger.error(f"Network error during translation: {str(e)}")
            raise TranslationError(f"Network error: {str(e)}")
        except ValueError as e:
            logger.error(f"Invalid language pair: {source_lang}-{target_lang}")
            raise TranslationError(str(e))
        except Exception as e:
            logger.error(f"Unexpected error during translation: {str(e)}")
            raise TranslationError(f"Translation failed: {str(e)}")


class TranslationError(Exception):
    pass
