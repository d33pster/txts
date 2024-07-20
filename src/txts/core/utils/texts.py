import re

class Normalizer:
    def __init__(self, text: str):
        self.text = text
    
    @property
    def normalize(self) -> str:
        self.text = self.text.lower()
        self.text = re.sub(r"\d+", lambda x: str(int(x.group(0))), self.text) # normalize number
        self.text = re.sub(r"\s+", ' ', self.text) # Replace multiple spaces with a single one.
        return self.text