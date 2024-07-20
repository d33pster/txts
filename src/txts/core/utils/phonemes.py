class Phonemes:
    dictionary = {
        'a': 'AA', 'b': 'B', 'c': 'K', 'd': 'D', 'e': 'EH', 'f': 'F',
        'g': 'G', 'h': 'HH', 'i': 'IH', 'j': 'JH', 'k': 'K', 'l': 'L',
        'm': 'M', 'n': 'N', 'o': 'OW', 'p': 'P', 'q': 'K', 'r': 'R',
        's': 'S', 't': 'T', 'u': 'UH', 'v': 'V', 'w': 'W', 'x': 'K',
        'y': 'Y', 'z': 'Z'
    }
    
    def __init__(self, text: str):
        self.text = text
    
    @property
    def get(self):
        return [self.dictionary.get(char, '') for char in self.text if char in self.dictionary]