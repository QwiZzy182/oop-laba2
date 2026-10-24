import re

class EmailValidator:
    def __init__(self):
        self.pattern = re.compile(r"\b[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,}\b")

    def validate_text(self, text: str) -> list:
        return self.pattern.findall(text)

    def validate_file(self, filepath: str) -> list:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return self.validate_text(f.read())
        except FileNotFoundError:
            return []
