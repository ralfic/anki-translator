import requests

class AnkiConnect:
    def __init__(self, base_url="http://localhost:8765"):
        self.base_url = base_url
        self.version = 6
        
    def _request(self, action, **params):
        payload = {'action': action, 'params': params, 'version': self.version}
        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            result = response.json()
            if result.get('error'):
                raise AnkiConnectError(result['error'])
            return result.get('result')
        except requests.exceptions.RequestException as e:
            raise AnkiConnectError(f"Connection error: {str(e)}")
    
    def get_decks(self):
        return self._request("deckNames")
    
    def get_models(self):
        return self._request("modelNames")
    
    def add_note(self, deck_name, model_name, fields, tags=None):
        note = {
            "deckName": deck_name,
            "modelName": model_name,
            "fields": fields,
            "options": {
                "allowDuplicate": False
            }
        }
        if tags:
            note["tags"] = tags
        return self._request("addNote", note=note)

class AnkiConnectError(Exception):
    pass