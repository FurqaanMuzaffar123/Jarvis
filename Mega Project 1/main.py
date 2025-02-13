import speech_recognition as sr
import pyaudio as pa
import webbrowser as wb
import pyttsx3 as v
import os
jarvis = v.init()
r = sr.Recognizer()
l = ["google","youtube","instagram","linkedin","facebook","twitter"]
songs = {
    "believer":"https://www.youtube.com/watch?v=W0DM5lcj6mw",
    "bones":"https://www.youtube.com/watch?v=ZNsPYmkSPeI",
    "enemy":"https://www.youtube.com/watch?v=hHB1Ikzfpmc",
    "victory anthem":"https://www.youtube.com/watch?v=0hJ4F-Nj5VY",
    "let me down slowly":"https://www.youtube.com/watch?v=jLNrvmXboj8",
    "alphabets":"https://www.youtube.com/watch?v=hq3yfQnllfQ"
}
def speak(text):
    jarvis.say(text)
    jarvis.runAndWait()
def output(c):
    if "exit" in c.lower():
        speak("Exiting..")
        os._exit(0)
    elif "jarvis" in c.lower():
        speak("Yes")
    for i in l:
        if f"open {i}" in c.lower():
            speak(f"Opening {i}...")
            wb.open(f"https://www.{i}.com/") 
    for i in songs:
        if f"play {i}" in c.lower():
            speak(f"playing {i}...")
            wb.open(songs[i])
speak("Initializing Jarvis....")
speak("Jarvis Active....")
while True:
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
            command = r.recognize_google(audio)
            output(command)
    except:
        pass

