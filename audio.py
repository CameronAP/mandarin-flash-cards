import requests
import json
from elevenlabs.client import ElevenLabs
from elevenlabs.play import save

EL_VOICE_ID = "<VOICE_ID>"
EL_API_KEY = "<API_KEY>"
CLIENT = ElevenLabs(api_key=EL_API_KEY)

# API endpoint and request formatting taken from testtovoice.online to directly request to their Audio generation endpoint
# This means it is not an official endpoint and this request is susceptible to changes made by testtovoice.
def text_to_voice_online(text):
    url = "https://www.texttovoice.online/"
    data = {
        "ttv_mode": "1",
        "bgMusic": "undefined",
        "userID": "<User_ID>", # get by going to the testtovoice and creating an account
        "provider": "aws",
        "text": text,
        "voice": "Zhiyu",
        "language": "cmn-CN",
        "speed": "100",
        "volume": "3",
        "exaggeration": "undefined",
        "usePremium": "0",
        "premium": "0",
        "voiceStyle": "neutral",
        "isEmotion": "0",
        "vol": "0.3",
        "rand": "20",
        "isSample": "0",
        "useSSML": "0",
        "voiceName": "Zhiyu",
        "isGem": "0",
        "speechPrompt": "undefined"
    }

    res_loc = requests.post(url + "scripts/awsRequest2.php", data=data)
    file_loc = json.loads(res_loc.content)["content"]

    res = requests.get(url + file_loc)
    return res.content

def text_to_voice_elevenlabs(text, filename , client = CLIENT):
    audio_data = client.text_to_speech.convert(
        text=text,
        voice_id=EL_VOICE_ID,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    save(audio=audio_data, filename= + filename)
