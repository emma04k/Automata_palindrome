import speech_recognition as sr

from tkinter import messagebox

class Recognition:

    def __init__(self):
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak Anything')
            audio = self.r.listen(source)

            try:
                text = self.r.recognize_google(audio)

                print(text)

            except:
                print('Sorry could not recognize your voice')


