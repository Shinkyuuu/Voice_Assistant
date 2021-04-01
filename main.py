import speech_recognition as sr
from notion.client import NotionClient
from notion.block import TodoBlock
import notion
import notion
import webbrowser
import playsound
import os
import time
import threading
import random
from gtts import gTTS
from datetime import date, datetime


os.system("cls")


#Open File
notionPath = "C:\\Users\\Cody\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\notion"
notionOpen = threading.Thread( target=os.startfile, args=(notionPath,))

githubPath = "C:\\Users\\Cody\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\GitHub Desktop"
githubOpen = threading.Thread(target=os.startfile, args=(githubPath,))


#Setup Notion
tokenv2='f443acf3104fc3090475db915c2b3d2a5ba7c19ae7985677cb29920aa077beb7b9e63b3785d17dc2f89ebf67cfee1ad1e0a5dc1ae632a12a5cd608f7439db945724eb7831c10e54cc92d053b5584'
notionClient = NotionClient(token_v2=tokenv2)
notionUrl = 'https://www.notion.so/Homework-89cc88c788254843bda8217cd56458e5'
page = notionClient.get_block(notionUrl)


def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    randomFileName = random.randint(1, 10000000)
    audio_file = "audio-" + str(randomFileName) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print("- " + audio_string)
    os.remove(audio_file)


def addToNotion(voice_data):
    cut_data = voice_data.split("add")
    cut_data = cut_data[1].split("to")
    newTask = page.children.add_new(TodoBlock, title=cut_data[0])

    if "sunday" in voice_data:
        block = notionClient.get_block('580c8cf6-3e31-41e6-8e8f-ae572ab5020d')
    elif "monday" in voice_data:
        block = notionClient.get_block('693553cb-19be-4a2e-9a75-45a4dec4ff38')
    elif "tuesday" in voice_data:
        block = notionClient.get_block('10eb90c4-c1ad-4779-b115-b22809c8fdd1')
    elif "wednesday" in voice_data:
        block = notionClient.get_block('c031801a-9653-49ec-a470-5e64048df3a7')
    elif "thursday" in voice_data:
            block = notionClient.get_block('0490faca-70e5-4b57-a2a7-1888bcd50fd6')
    elif "friday" in voice_data:
        block = notionClient.get_block('4cf5d4c8-3021-4605-a670-627c6a1563d8')
    elif "saturday" in voice_data:
            block = notionClient.get_block('0490faca-70e5-4b57-a2a7-1888bcd50fd6')

    newTask.move_to(block, "after")


def todayDate():
    today = date.today()
    return today.strftime("%B %d, %Y")

def todayTime():
    time = datetime.now()

    return time.strftime("%I:%M %p")

def record():
    print("~~~~recording~~~~")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("~~~~start listening~~~~")
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError:
            speak("Sorry, my I am down currently!")

        return voice_data


def respond(voice_data):
    voice_data = voice_data.lower()
    print("> " + voice_data)
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

    if  "open" in voice_data:
        if  "ocean" in voice_data or "notion" in voice_data:
            notionOpen.start()
        elif "GitHub" in voice_data:
            githubOpen.start()
    
    if "add" in voice_data:
        addToNotion(voice_data)

    if "notion data" in voice_data:
        for child in page.children:
            try:
                print(child.title)
            except:
                print(child.id)
                for baby in child.children:
                    try:
                        print(baby.title)
                    except:
                        print(baby.id)
                        for fetus in baby.children:
                            try:
                                print(fetus.title)
                            except:
                                print(fetus.id)
            
        
    if "off" in voice_data:
        speak("Ok.")
        exit()

# for child in page.children:
#     try:
#         print(child.title)
#     except:
#         print(child.id)
#         for baby in child.children:
#             try:
#                 print(baby.title)
#             except:
#                 print(baby.id)
#                 for fetus in baby.children:
#                     try:
#                         print(fetus.title)
#                     except:
#                         print(fetus.id)
block = notionClient.get_block('693553cb-19be-4a2e-9a75-45a4dec4ff38')
while True:
    voice_data = record()
    
    if "kimchi" in voice_data:
        speak("Yes")

        voice_data = record()
        respond(voice_data)


