import pyaudio
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Talk now")
    audio_data = r.record(source, duration=5)
    print("Computing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
