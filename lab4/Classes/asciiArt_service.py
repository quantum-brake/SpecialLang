from Classes.fileSaver import FileManager
from Classes.asciiArt_displayer import ArtDisplayer
from Classes.userInput_handler import UserInputManager


class AsciiArtService:
    def __init__(self):
        self.file_manager = FileManager()
        self.art_displayer = ArtDisplayer()
        self.user_input_manager = UserInputManager()
        self._ascii_generator = self.user_input_manager.ascii_generator

    def generate_ascii_art(self):
        return self._ascii_generator.generate_art()

    def update_text(self):
        return self.user_input_manager.update_text()

    def update_color(self):
        self.art_displayer.colorizer.list_colors()
        self.art_displayer.colorizer.update_color()

    def update_width(self):
        return self.user_input_manager.update_width()

    def update_height(self):
        return self.user_input_manager.update_height()

    def update_alignment(self):
        return self.user_input_manager.update_alignment()

    def display_ascii_art(self):
        ascii_art = self.generate_ascii_art()
        self.art_displayer.display_art(ascii_art, self._ascii_generator.get_width(), len(self._ascii_generator.get_text()),
                                       self._ascii_generator.get_alignment(), self.art_displayer.colorizer.get_color())

    def save_ascii_art(self):
        ascii_art = self.generate_ascii_art()
        filename = input("Введіть назву файла в який хочете зберегти ASCII art (наприклад, art.txt): ")
        self.file_manager.save_to_file(ascii_art, filename)
