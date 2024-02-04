import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


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
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScarp
        query = query.replace("jarvis","")
        query = query.replace("sachi","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")
        
        try:
            pywhatkit.search(query)
            result = googleScarp.summary(query,1)
            speak(result)
        except:
            speak("No speakable output available")

def searchYutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("YouTube search","")
        query = query.replace("YouTube","")
        query = query.replace("jarvis","")
        query = query.replace("sachi","")
        web = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done,sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching form wikipedia......")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        query = query.replace("sachi","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia...")                
        print(results)
        speak(results)