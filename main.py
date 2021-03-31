import speech_recognition as sr
from notion.client import NotionClient
import webbrowser
import playsound
import os
import time
import threading
import random
from gtts import gTTS
from datetime import date, datetime


#Open File
notionPath = "C:\\Users\\Cody\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\notion"
notionOpen = threading.Thread( target=os.startfile, args=(notionPath,))

githubPath = "C:\\Users\\Cody\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\GitHub Desktop"
githubOpen = threading.Thread(target=os.startfile, args=(githubPath,))


#Setup Notion
client = NotionClient(token_v2="f443acf3104fc3090475db915c2b3d2a5ba7c19ae7985677cb29920aa077beb7b9e63b3785d17dc2f89ebf67cfee1ad1e0a5dc1ae632a12a5cd608f7439db945724eb7831c10e54cc92d053b5584")
# page = client.get_block("https://www.notion.so/Cody-bf8d89e1339c4f47a0661dd75a0e7624")


#Setup Audio Recogizer



def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    randomFileName = random.randint(1, 10000000)
    audio_file = "audio-" + str(randomFileName) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def todayDate():
    today = date.today()
    return today.strftime("%B %d, %Y")

def todayTime():
    time = datetime.now()

    return time.strftime("%I:%M %p")

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Did you say somthing")
        except sr.RequestError:
            speak("Sorry, my I am down currently!")

        return voice_data


def respond(voice_data):
    print(voice_data)

    if "banana bread" in voice_data:
        speak("I love banana bread")

    if "today" and "date" in voice_data:
        speak("Today's date is " + todayDate())

    if "what time" in voice_data:
        speak("It is currently " + todayTime())

    if "look" and "up" in voice_data:
        speak("What would you like to search?")
        search = record()
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Here is " + search + "!")

    if "open" in voice_data:
        if "ocean" in voice_data:
            notionOpen.start()
        elif "GitHub" in voice_data:
            githubOpen.start()

    if "off" in voice_data:
        speak("Ok, see you later!")
        exit()
    

while True:
    voice_data = record()
    print("recording ")
    if "kimchi" in voice_data:
        speak("beep boop")

        voice_data = record()
        print("recording 2")
        respond(voice_data)


