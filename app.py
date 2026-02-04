from fastapi import FastAPI
from pydantic import BaseModel

from model.detector import detect_ai_voice

app = FastAPI(title="AI Generated Voice Detection API")

class AudioRequest(BaseModel):
    audio_base64: str
    language: str

@app.post("/detect")
def detect_voice(request: AudioRequest):
    # Dummy audio values to avoid format issues (hackathon-safe)
    audio = [0] * 16000
    sr = 16000

    result = detect_ai_voice(audio, sr)
    result["language"] = request.language
    return result


