import base64
import io
import librosa

def base64_to_wav(base64_audio):
    audio_bytes = base64.b64decode(base64_audio)
    audio_buffer = io.BytesIO(audio_bytes)
    audio, sample_rate = librosa.load(audio_buffer, sr=16000)
    return audio, sample_rate
