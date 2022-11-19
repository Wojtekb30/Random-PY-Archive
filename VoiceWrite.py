import time
import pyaudio
import pyautogui
import os
import speech_recognition as sr
r = sr.Recognizer()
print("Start in 10 seconds, say END or FINISH to close, say SEND to press ENTER")
time.sleep(10)
while 1==1:
    try:
        with sr.Microphone() as source:
            print("Recording for 5 seconds...")
            audio_data = r.record(source, duration=5)
            print("Computing...")
            #inp = r.recognize_google(audio_data, language='pl')
            inp = r.recognize_google(audio_data)
            print(inp)
            if inp.upper()=='END' or inp.upper()=='FINISH' or inp.upper()=='AND':

            
                break
            if inp.upper()=='SEND':
                pyautogui.press('enter')
            else:
                inp=inp+" "
                pyautogui.write(inp)
            inp = ""
    except:
        print("ERR")
        inp = ""
