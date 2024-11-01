from transformers import pipeline

asr = pipeline("automatic-speech-recognition", model="openai/whisper-base")

audio_file = "audio_path_file.wav"

print("Transcribed Text:", asr(audio_file)["text"])
