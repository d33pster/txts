import numpy as np
import sounddevice as sd
import wave
import struct

from txts.core.utils.phonemes import Phonemes
from txts.core.utils.texts import Normalizer

class Wave:
    FREQUENCIES = {
        'AA': 700, 'B': 500, 'K': 800, 'D': 600, 'EH': 900, 'F': 1000,
        'G': 1100, 'HH': 1200, 'IH': 1300, 'JH': 1400, 'L': 1500, 'M': 1600,
        'N': 1700, 'OW': 1800, 'P': 1900, 'R': 2000, 'S': 2100, 'T': 2200,
        'UH': 2300, 'V': 2400, 'W': 2500, 'Y': 2600, 'Z': 2700
    }

    def __init__(self, text: str):
        self.text = text
        self.wave: np.ndarray
    
    def _generate_wave(self, frequency: float, duration: float, sample_rate: int = 44100) -> np.ndarray:
        intermediate = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        return 0.5 * np.sin(2 * np.pi * frequency * intermediate)
    
    def _phoneme_to_wave(self, phoneme: str) -> np.ndarray:
        frequency = self.FREQUENCIES.get(phoneme, 0)
        return self._generate_wave(frequency=frequency, duration=0.5)

    @property
    def synthesize(self):
        self.text = Normalizer(self.text).normalize
        self.phonemes = Phonemes(self.text).get
        
        waves = [self._phoneme_to_wave(phoneme) for phoneme in self.phonemes]

        self.wave = np.concatenate(waves)
    
    @property
    def get(self):
        return self.wave

    @property
    def play(self):
        sample_rate: int = 44100
        sd.play(self.wave, samplerate=sample_rate)
        sd.wait()
    
    N_CHANNELS = 1
    SAMPWIDTH = 2
    COMPTYPE = "NONE"
    COMPNAME = "not compressed"

    def save(self, filename: str, sample_rate: int = 44100):
        with wave.open(filename, "w") as wav_file:
            wav_file.setparams((self.N_CHANNELS, self.SAMPWIDTH, sample_rate, len(self.wave), self.COMPTYPE, self.COMPNAME))
            for s in self.wave:
                wav_file.writeframes(struct.pack('h', int(s * 32767)))
    