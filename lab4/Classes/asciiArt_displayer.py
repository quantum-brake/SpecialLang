from Classes.asciiArt_colorizer import Colorizer


class ArtDisplayer:
    def __init__(self):
        self.colorizer = Colorizer()

    def display_art(self, ascii_art, width, text_length, alignment, color):
        for line in ascii_art:
            aligned_line = self.align_line(line, width * text_length, alignment)
            if color:
                aligned_line = self.colorizer.colorize(aligned_line, color)
            print(aligned_line)

    def align_line(self, line, width, alignment):
        if alignment == 'left':
            return line.ljust(width)
        elif alignment == 'center':
            return line.center(width)
        elif alignment == 'right':
            return line.rjust(width)
        return line

