import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def latestnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=ad8427b3c9f849879f846e2ab45e77ba",
                "entertainement":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=ad8427b3c9f849879f846e2ab45e77ba",
                "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=ad8427b3c9f849879f846e2ab45e77ba",
                "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=ad8427b3c9f849879f846e2ab45e77ba",
                "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=ad8427b3c9f849879f846e2ab45e77ba",
                "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=ad8427b3c9f849879f846e2ab45e77ba"
                
}
    
    content = None
    url = None
    speak("wich feild news do you want, [business] , [health], [technology], [sports], [entertainment],[science]")
    field = input("Type field news that you want: ") 
    for key , value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")  
                
    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")
    
    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)  
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        
        a = input("[press 1 to continue] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("That's all")          