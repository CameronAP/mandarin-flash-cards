import re
from audio import text_to_voice_online, text_to_voice_elevenlabs

class tts_types:
    online = "online"
    elevenlabs = "elevenlabs"

tts_func_map = {
    tts_types.online: text_to_voice_online,
    tts_types.elevenlabs: text_to_voice_elevenlabs
}
def create_card(row):
    chars = re.sub(r'([?!\.]+)', r'\1 ', re.sub(r'[^\w\(\)\?\!\.\,\-]+', "", row[0])).strip()
    pinyin = re.sub(r'([?!\.]+)', r'\1 ', re.sub(r'[^\w\(\)\?\!\.\,\-]+', "", row[1])).strip()
    english = re.sub(r'[^\w\(\)\?\!\.\, ]+', "", row[2]).strip()

    audio = tts_func_map[tts_types.online](chars)

    filename = re.sub(r"\W+", "", english) + ".mp3"
    etc_front = english
    etc_back = f'{chars}<br><div class="pinyin">{pinyin}</div>'
    ctpy_front = chars
    ctpy_back = f"<div>{pinyin}<div>"
    return {
        "filename": filename,
        "audio": audio,
        "eng_to_char": {"front": etc_front, "back": etc_back},
        "char_to_pnyn": {"front": ctpy_front, "back": ctpy_back}
    }