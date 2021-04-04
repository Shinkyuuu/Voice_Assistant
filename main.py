#gtts
#playsound
#pipwin
#pyaudio
#speechrecognition
#notion

import speech_recognition as sr
import webbrowser
import playsound
import os
import time
import threading
import random
from gtts import gTTS
from datetime import date, datetime
import notionReq as nq


#~~~~~~~~~~~~~~~~Open Files~~~~~~~~~~~~~~~~#
notionPath = "C:\\Users\\cody\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\notion"
notionOpen = threading.Thread( target=os.startfile, args=(notionPath,))

githubPath = "C:\\Users\\cody\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\GitHub, Inc\\GitHub Desktop"
githubOpen = threading.Thread(target=os.startfile, args=(githubPath,))


#~~~~~~~~~~~~~Specialized Functions~~~~~~~~~~~~~#
def todayDate():
    today = date.today()
    return today.strftime("%B %d, %Y")


def todayTime():
    time = datetime.now()
    return time.strftime("%I:%M %p")


#~~~~~~~~~~~~~~~Core Functions~~~~~~~~~~~~~~~#
def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en", tld="com")
    randomFileName = random.randint(1, 10000000)
    audio_file = "audio-" + str(randomFileName) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print("- " + audio_string)
    os.remove(audio_file)


def record():
    r = sr.Recognizer()
    print("~~~~recording~~~~")
    with sr.Microphone() as source:
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

    if "today" and "date" in voice_data:
        speak("Today's date is " + todayDate())

    if "what time" in voice_data:
        speak("It is currently " + todayTime())

    if ("look"  in voice_data) and ("up" in voice_data):
        speak("What would you like to search?")
        search = record()
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Here is " + search + "!")

    if  "open" in voice_data:
        try:
            if  "ocean" in voice_data or "notion" in voice_data:
                notionOpen.start()
            elif "GitHub" in voice_data:
                githubOpen.start()
        except:
            speak("Sorry, I couldn't find it.")
    
    if "add" in voice_data:
        result = nq.addToNotion(voice_data)
        speak(result)

    if "notion data" in voice_data:
        speak("Printing notion data")
        nq.printNotionData()

    if ("uncheck" not in voice_data) and ("check" in voice_data):
        result = nq.checkTask(voice_data)
    
    if "uncheck" in voice_data:
        result = nq.unCheckTask(voice_data)
        
    if "off" in voice_data:
        speak("Ok.")
        exit()


#~~~~~~~~~~~~~~~~~Main Loop~~~~~~~~~~~~~~~~~#
if __name__ == "__main__":
    os.system("cls")
    speak("Kimchi online!")
    # nq.addToNotion("add cs303 notes to sunday")
    # nq.addToNotion("add cs303 test to tuesday")
    # nq.addToNotion("add test to tuesday")
    # nq.addToNotion("add cs303 test")
    # nq.addToNotion("add test")
    while True:
        voice_data = record()
        
        if "kimchi" in voice_data:
            speak("Yes?")
            voice_data = record()
            respond(voice_data)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#