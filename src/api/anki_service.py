import requests


class AnkiService:
    def __init__(self, base_url: str = "http://localhost:8765"):
        self.base_url = base_url
        self.version = 6

    def _request(self, action, **params):
        payload = {"action": action, "params": params, "version": self.version}
        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            result = response.json()
            if result.get("error"):
                raise AnkiConnectError(result["error"])
            return result.get("result")
        except requests.exceptions.RequestException as e:
            raise AnkiConnectError(f"Connection error: {str(e)}")

    def get_decks(self):
        return self._request("deckNames")

    def get_models(self):
        return self._request("modelNames")

    def add_note(self, deck_name: str, model_name: str, fields: str, tags=None):
        note = {
            "deckName": deck_name,
            "modelName": model_name,
            "fields": fields,
            "options": {"allowDuplicate": False},
        }

        if tags:
            note["tags"] = tags

        can_add_note = self._request("canAddNotesWithErrorDetail", notes=[note])
        res = can_add_note[0]

        if res.get("error") is None and res.get("canAdd") is True:
            return self._request("addNote", note=note)
        else:
            raise AnkiConnectError(res.get("error"))


class AnkiConnectError(Exception):
    pass
