from art import text2art


class ASCIIGenerator:
    def __init__(self, text, font="roman", custom_char=None):
        self.text = text
        self.font = font
        self.custom_char = custom_char
        self.ascii_art = self.generate_ascii_art()

    def generate_ascii_art(self):
        ascii_art = text2art(self.text, font=self.font)

        if self.custom_char:
            ascii_art_lines = []
            for char in ascii_art:
                if char != ' ' and char != '\n':
                    ascii_art_lines.append(self.custom_char)
                else:
                    ascii_art_lines.append(char)

            ascii_art = ''.join(ascii_art_lines)

        return ascii_art

    def scale_art(self, width, height):
        lines = self.ascii_art.split('\n')
        scaled_art = ""

        for line in lines:
            scaled_line = ''.join([char * width for char in line])
            scaled_art += scaled_line + '\n' * height

        return scaled_art

