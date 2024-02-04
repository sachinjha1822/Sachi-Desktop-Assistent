import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Say that again")
        speak("say that again")
        return "None"
    return query
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("who do you want to message")
    a = int(input('''
    Person 1 - 1 
    person 2 - 2 '''))
    if a == 1:
        speak("What's the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+9100000000000",message,time_hour=strTime,time_min=update)
    elif a == 2:
        speak("What's the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+9100000000000",message,time_hour=strTime,time_min=update)
