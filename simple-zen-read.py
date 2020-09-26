from dataclasses import dataclass

@dataclass
class TextFile:
    file: str

    def read(self):
        with open(self.file) as f:
            self.text = f.read()
