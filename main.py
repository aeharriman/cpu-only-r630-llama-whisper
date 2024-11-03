import whisper
import pyaudio
import wave
from transformers import AutoModelForCausalLM, AutoTokenizer
from gtts import gTTS
import os

def record_audio(filename, duration=5):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Done recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe_audio(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]

def generate_text(prompt):
    model_name = "meta-llama/LLaMA-2-7b"  # Replace with your specific LLaMA model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"start {filename}")  # Use 'afplay' on macOS, 'start' on Windows, 'xdg-open' on Linux

if __name__ == "__main__":
    audio_file = "recording.wav"
    response_audio_file = "response.mp3"

    record_audio(audio_file)
    transcription = transcribe_audio(audio_file)
    print(f"Transcription: {transcription}")

    generated_text = generate_text(transcription)
    print(f"Generated Text: {generated_text}")

    text_to_speech(generated_text, response_audio_file)
