from backend.speech.whisper_service import transcribir_audio

texto = transcribir_audio(
    "audio_prueba.wav"
)

print(texto)