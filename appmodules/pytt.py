import pyttsx3

class Pytt:

    def __init__(self, text):
        self.text = text
        self.engine = pyttsx3.init()
        self.engine.getProperty('volume')
        self.engine.getProperty('rate')
        self.engine.getProperty('voice')

        self.engine.setProperty('volume',3)
        self.engine.setProperty('rate',160)
        self.listvoices = self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.listvoices[1].id)

        self.engine.say(text)
        self.engine.runAndWait()