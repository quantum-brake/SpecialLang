import os


class CharacterLoader:
    def __init__(self):
        self.char_set = {}
        self._character_directory = os.path.join(os.path.dirname(__file__), "../Assets")
        self.load_characters()
        self._filename = ""

    def load_characters(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#_+-,. ":
            if char.isalpha():
                if char.isupper():
                    self._filename = os.path.join(self._character_directory, f"letters/{char}{char}.txt")
                elif char.islower():
                    self._filename = os.path.join(self._character_directory, f"letters/{char}.txt")
            elif char.isdigit():
                self._filename = os.path.join(self._character_directory, f"numbers/{char}.txt")
            else:
                self._filename = os.path.join(self._character_directory, f"symbols/{char}.txt")

            if os.path.exists(self._filename):
                with open(self._filename, 'r') as file:
                    self.char_set[char] = [line.rstrip('\n') for line in file.readlines()]
            else:
                self.char_set[char] = [' ' * 10] * 10


