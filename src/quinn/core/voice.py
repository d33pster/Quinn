from gtts import gTTS
from playsound import playsound
from os.path import expanduser, join
from os import makedirs, unlink

from quinn.core.Files.names import Name

class Voice:
    def __init__(self):
        self.config = join(expanduser("~"), ".quinn", "replies")
        makedirs(self.config, exist_ok=True)

        self.name = Name(type="reply", directory=self.config)
    
    def speak(self, text: str):
        tts = gTTS(text=text, tld="co.in")
        reply_path = join(self.config, self.name.assign)
        tts.save(reply_path)
        playsound(reply_path)
        unlink(reply_path)