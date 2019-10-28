from gtts import gTTS
import os

class Synthesis_voice:

    def __init__(self, message):
        self.message = message
        self.audio_name = 'audio1.mp3'

        self.tts = gTTS(self.message, lang='es-us')

        with open(self.audio_name,"wb") as archivo:
            self.tts.write_to_fp(archivo)

        os.system('mpg123 '+self.audio_name)

