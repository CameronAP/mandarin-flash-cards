import requests
import base64
ANKI_CONNECT_URL = "http://localhost:8765"

def invoke(action, **params):
    try:
        res = requests.post(
        ANKI_CONNECT_URL,
        json={"action": action, "version": 6, "params": params}
    ).json()
    except Exception as e:
        res = {"error": e}
    return res

def get_anki_decks():
    res = invoke("deckNames")
    error = res["error"]
    if error != None:
        raise ConnectionError(error)
    return res["result"]

def add_card_with_audio_bytes(deck_name: str, front: str, back: str, audio_bytes: bytes, filename: str):
    b64_data = base64.b64encode(audio_bytes).decode("utf-8")
    invoke("storeMediaFile", filename=filename, data=b64_data)

    note = {
        "deckName": deck_name,
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": f"{back} [sound:{filename}]"
        },
        "tags": ["auto", "audio"]
    }
    res = invoke("addNote", note=note)
    return res