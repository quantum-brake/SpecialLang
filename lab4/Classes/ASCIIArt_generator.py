from Classes.characterLoader import CharacterLoader


class ASCIIGenerator:
    def __init__(self):
        self.character_loader = CharacterLoader()
        self.char_set = self.character_loader.char_set
        self._width = 13
        self._height = 8
        self._text = "Hello World!"
        self._alignment = "center"

    def generate_art(self):
        ascii_lines = ['' for _ in range(self._height)]

        for char in self._text:
            char_lines = self.char_set.get(char, [' ' * self._width] * self._height)

            if len(char_lines) < self._height:
                char_lines += [' ' * self._width] * (self._height - len(char_lines))

            for i in range(self._height):
                ascii_lines[i] += char_lines[i] + ' '
        return ascii_lines

    def set_text(self, text):
        self._text = text

    def get_text(self):
        return self._text

    def set_width(self, width):
        self._width = width

    def get_width(self):
        return self._width

    def set_height(self, height):
        self._height = height

    def get_height(self):
        return self._height

    def set_alignment(self, alignment):
        self._alignment = alignment

    def get_alignment(self):
        return self._alignment
