import speech_recognition
r = speech_recognition.Recognizer( )

with speech_recognition.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    voice_data = recognize_google(audio)
    print(voice_data)

