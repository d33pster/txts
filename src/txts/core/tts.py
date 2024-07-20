from txts.core.utils.waves import Wave

class TTS:
    def __init__(self):
        pass
    
    def say(self, text: str = "hello"):
        self.wave = Wave(text=text)
        self.wave.synthesize
        self.wave.play