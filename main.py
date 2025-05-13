import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "YOUR-API"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    if "open google maps" in c.lower():
        webbrowser.open("https://www.google.com/maps")
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=d7d2e6d04da744f6bb61f7b2abb13fb5")

        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            
            print("Top Headlines:\n")
            for idx, article in enumerate(articles[:10], start=1):  # Show top 10 headlines
                print(f"{idx}. {article['title']}")
                speak(f"{idx}. {article['title']}")
        else:
            print(f"Failed to fetch news: {response.status_code}")



if __name__=="__main__":
    speak("Initializing Veer......")
    while True:
        # listen for the wake word Veer
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Say something...")
                audio = r.listen(source)
            initial_call = r.recognize_google(audio)
            print("You said:", initial_call)
            if ("veer" in initial_call.lower()):
                speak("Listening Sir")
                # listen for command
                with sr.Microphone() as source:
                    print("Veer is listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
