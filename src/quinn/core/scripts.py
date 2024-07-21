from quinn.core.voice import Voice
from quinn.core.soul import Soul

from datetime import datetime
from os import getlogin



import speech_recognition

class Scripts:
    def __init__(self):
        self.master: str = getlogin()
        self.voice = Voice()
        self.soul = Soul()
    
    @property
    def wish(self):
        hour = int(datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.voice.speak("Good Morning Sir!")
        elif hour >= 12 and hour <= 18:
            self.voice.speak("Good Afternon Sir!")
        else:
            self.voice.speak("Good Evening Sir!")
        
        self.voice.speak(self.soul.name + ". At your service Sir!")
    
    @property
    def accept_command(self) -> str:
        sr = speech_recognition.Recognizer()

        with speech_recognition.Microphone() as source:
            print("\nListening.", end="")
            sr.pause_threshold = 1
            audio = sr.listen(source)
        
        try:
            return sr.recognize_bing(audio_data=audio)
        except Exception as e:
            print(e)
            return "None"
    
    @property
    def call(self) -> bool:
        