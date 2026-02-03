from fastapi import FastAPI
from pydantic import BaseModel

from utils.audio_utils import base64_to_wav
from model.detector import detect_ai_voice

app = FastAPI(title="AI Generated Voice Detection API")

class AudioRequest(BaseModel):
    audio_base64: str
    language: str

@app.post("/detect")
def detect_voice(request: AudioRequest):
    audio, sr = base64_to_wav(request.audio_base64)
    result = detect_ai_voice(audio, sr)
    result["language"] = request.language
    return result
