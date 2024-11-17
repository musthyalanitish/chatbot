import sounddevice as sd
import numpy as np
import speech_recognition as sr
import io
from scipy.io.wavfile import write

def mic1():
    samplerate = 44100  # Hertz
    duration = 7  # seconds
    print("Say something:")

    try:
        audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        print("Recording complete. Recognizing...")

        audio_buffer = io.BytesIO()
        write(audio_buffer, samplerate, audio_data)
        audio_buffer.seek(0)

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_buffer) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; check your internet connection. Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
