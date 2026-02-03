from transformers import pipeline

classifier = pipeline(
    "audio-classification",
    model="facebook/wav2vec2-base"
)

def detect_ai_voice(audio, sample_rate):
    prediction = classifier({
        "array": audio,
        "sampling_rate": sample_rate
    })

    top = prediction[0]
    label = top["label"]
    confidence = float(top["score"])

    is_ai_generated = False
    if "fake" in label.lower() or "synthetic" in label.lower():
        is_ai_generated = True

    return {
        "is_ai_generated": is_ai_generated,
        "confidence": round(confidence, 2),
        "explanation": f"Voice characteristics matched with {label}"
    }
