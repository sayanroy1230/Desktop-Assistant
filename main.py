import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import speech_recognition as sr
import signal
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    else:
        speak("good night")
    speak("Hi i'm Jarvis please tell me how may i help you")
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        # speak("listening...")
        r.pause_threshold=0.8
        audio=r.listen(source)
    try:
        print("Recognizing...")
        # speak("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say That Again please...")
        speak("Say That Again please...")
        return "None"
    return query

def signal_handler(sig, frame):
    print('Goodbye')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

wishme()
while True:
    query=takecommand().lower()
    if 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("according to wikipedia...")
        speak(result)
        print(result)
    elif "open youtube" in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")
    elif "open google" in query:
        speak("opening google")
        webbrowser.open("google.com")
    elif "play music" in query:
        musicdir=r"C:\Users\SAYAN ROY\OneDrive\Desktop\chatroom using prompt\public"
        song="whatsapp.mp3"
        os.startfile(os.path.join(musicdir,song))
    elif "time" in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(strtime)
    elif "open code" in query:
        vscode=r"C:\Users\SAYAN ROY\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(vscode)
    
