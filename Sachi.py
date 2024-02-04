import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup
import pyautogui
import keyword
import random
from plyer import notification
from pygame import mixer
import speedtest

for i in range(3):
    a = input("Enter Password to open Sachi:- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("Welcome sir! please speak [wake up] to load me up")
        break
    elif (i==2 and a!=pw):
        exit()
        
    elif (a!=pw):
        print("Try again!")
        
        
#from INTRO import play_gif
#play_gif

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
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

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Okay Sir, You can call me anytime")
                    break
                
                ############################## Sachi: The Triology 2.0 ########################################
                
                elif "change password" in query:
                    speak("What's the new Password")
                    new_pass = input("Enter the new Password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pass)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new Passeord is {new_pass}")
                
                elif "schedule my day" in query:
                    tasks = [] #Empty list
                    speak("Do you want to clear old tasks (Plz speak yes or no)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no of tasks:- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task:- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no of tasks:- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task:- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                            
                elif "my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("Notification - Notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title ="My schedule:- ",
                        message = content, 
                        timeout = 15
                    )
                
                elif "focus mode" in query:
                    speak("are you sure that you want to enter focus mode please press 1 or 2 and enter")
                    a = int(input("Are you sure that you want to enter focus mode:- [1 for yes / 2 for No]:- "))
                    if (a == 1):
                        speak("Entering the focus mode....")
                        from FocusMode import is_admin
                        is_admin()
                    else:
                        pass
                    
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                    
                    
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    query = query.replace(" ","")
                    translategl(query)
                    
                    
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("Sachi","")
                    query = query.replace("please","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                    
                elif "screenshot" in query or "take screenshot" in query:
                    query = query.replace("open","")
                    query = query.replace("Sachi","")
                    query = query.replace("please","")  
                    pyautogui.keyDown("ctrl","w")

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576
                    download_net = wifi.download()/1048576
                    print("wifi download speed is",download_net)
                    print("wifi upload speed is",upload_net)
                    speak(f"wifi download speed is {download_net}M b")
                    speak(f"wifi uplload speed is {upload_net}M b")  
                    
                elif "ipl score" in query:
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()           
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()  
                    team1_score = soup.find_all(class_ = "cb-over-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-over-flo")[10].get_text()
                    
                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")
                    
                    notification.notify(
                        title = "IPL Score:- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 10
                    )
                
                elif "play a game" in query:
                    from game import game_play
                    game_play()
                
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.sleep(1)
                    pyautogui.typewrite("camera")
                    pyautogui.sleep(1)
                    pyautogui.press("enter")
                    pyautogui.sleep(10)
                    speak("SMILE")
                    pyautogui.press("enter")
                   
                 
                elif "knowing the birth" in query:
                    from BirthDate import ask_question
                    ask_question() 
                    
                ###############################################################################################
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("Thats great, sir")
                elif "how r u" in query or "how are you" in query:
                    speak("Perfect Sir")
                elif "thank" in query:
                    speak("You are welcome,sir")
                elif "bolo" in query:
                    speak("Jaai shree Raam")
                
                elif "exam" in query or "examination" in query:
                    speak("Good luck with your exams!")
                elif "tired" in query:
                    speak("Playing your favourite songs")
                    a =(1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=Zlqf9cuaOBw")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=OBEOPnAO1hc")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=6OXfgu8uKnEmm")
                        
                elif "good morning" in query:
                    speak("Many good morning Sir")
                elif "good afternoon" in query:
                    speak("Many goodafter noon Sir")
                elif "good evening" in query:
                    speak("Many good evening Sir")
                    
                elif "open" in query:
                    from DictApp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from DictApp import closeappweb
                    closeappweb(query)
                 
                elif "pause video" in query or "pause" in query:
                    pyautogui.press("k")
                    speak("Video paused")
                elif "play video" in query or "play" in query:
                    pyautogui.press("k")
                    speak("Video played")
                elif "mute video" in query:
                    pyautogui.press("m")
                    speak("video mute")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmute")
                    
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down,sir")
                    volumedown()
                elif "volume mute" in query:
                    from keyboard import volumedown
                    speak("volume muted,sir")
                    volumedown()   
                    
                    
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "YouTube" in query:
                    from searchNow import searchYutube
                    searchYutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("Sachi","")
                    Calc(query)
                    
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                elif "temperature" in query:
                    search = "temprature in mathura"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data .find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in mathura"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data .find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif "set an alarm" in query or "set alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("Please ttell the time:- ")
                    alarm(a)
                    speak("done,Sir")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                
                elif "finally sleep" in query:
                    speak("okay good bye i am Going to sleep, sir, Have a Great day!")
                    exit()
                    
                elif "what is my father's name" in query:
                    mtname = open("fathersname.txt","r")
                    speak("Your Father's name is" + mtname.read())
                elif "what is my mother's name" in query:
                    mtname = open("mothersname.txt","r")
                    speak("Your Mother's name is" + mtname.read())
                elif "birth date" in query or "birthday" in query or "budday" in query or "date of birth" in query:
                    btname = open("birthdate.txt","r")
                    speak("Your Birth date is" + btname.read())
                elif "wish me" in query or "vish " in query:
                    query = query.replace("sachi","")
                    wishme = open("wishMe.txt","r")
                    speak("Okay" + wishme.read())
                    
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    rememberMessage = query.replace("sachi","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me  to " + remember.read())
                    
                elif "shutdown system" in query:
                    speak("Are you want to shutdown")
                    shutdown = input("Do yoou wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
