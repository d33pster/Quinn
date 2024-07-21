import numpy
import sounddevice
import speech_recognition
import time as t
import scipy.io.wavfile as wavfile

class Call:
    def __init__(self, keyword: str = "queen", duration: int = 5, silence_timeout: int = 3, sample_rate: int = 44100):
        self.keyword = keyword
        self.duration = duration
        self.sample_rate = sample_rate
        self.silence_timeout = silence_timeout

    def detect(self) -> bool:
        recognizer = speech_recognition.Recognizer()
        last_speech_time = t.time()

        audio_buffer = []

        def callback(indata, frames, time, status):
            nonlocal last_speech_time
            if status:
                print(f"Error: {status}")
            
            if numpy.max(numpy.abs(indata)) > 0.01:
                print("Detecting!")
                audio_buffer.append(indata.copy())
                last_speech_time = t.time()
            else:
                if t.time() - last_speech_time > self.silence_timeout:
                    return sounddevice.CallbackStop

        
        # start monitoring
        with sounddevice.InputStream(callback=callback, channels=1, samplerate=self.sample_rate):
            print("Quinn listening ...")
            try:
                while True:
                    t.sleep(1)
            except sounddevice.CallbackStop:
                print("Analysing")
                if audio_buffer:
                    full_audio = numpy.concatenate(audio_buffer, axis=0)

