import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from groq import Groq
from AppOpener import open, features, close

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "188c9b33da0f4c909dc4616f31918c64"


def speak(text):
    engine.say(text)
    engine.runAndWait()


# for ai search


def aiProcess(command):

    client = Groq(
        # This is the default and can be omitted
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a Virtual assistant named jarvis skilled in general tasks like alexa and google cloud. give short responce  ",
            },
            {
                "role": "user",
                "content": command,
            },
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content


def opneAplication(app):
    try:
        open(app, match_closest=True, throw_error=True)

    except features.AppNotFound as e:
        speak("Can not found")


def closeApplication(app):
    try:
        close(app,output=False, match_closest=True, throw_error=True)

    except features.AppNotFound as e:
        speak("Can not found")


def processCommand(c):

    # opening web
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open my resume" in c.lower():
        webbrowser.open("https://harshilresume.netlify.app/")

    # paly music
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        # print(song, link)
        speak(f"palying {song}", )
        webbrowser.open(link)

    # Get news
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=188c9b33da0f4c909dc4616f31918c64")

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])

            for article in articles:
                speak(article["title"])

    # Open Application
    elif c.lower().startswith("open"):
        app = c.split(" ")[1]
        opneAplication(app)

    # Close Application
    elif c.lower().startswith("close"):
        app = c.split(" ")[1]
        closeApplication(app)

    # work with open ai
    else:
        optput = aiProcess(c)
        speak(optput)


if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:
        # jarvis bolo to responce
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Ya")

                # command aapvano ape
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Main Error {0}".format(e))
            # speak("sorry i can't do this")
