from Classes.Ascii_art_generator import ASCIIGenerator
from Classes.Error_handler import ErrorHandler
from Classes.File_saver import FileManager
from Classes.Color_handler import ColorHandler


class ASCIIArtService:
    def __init__(self):
        self.error_logger = ErrorHandler()
        self.file_manager = FileManager()
        self.color_handler = ColorHandler()

    def generate_ascii_art(self, text, font, custom_char, width, height, color):
        self.error_logger.validate_text_input(text)

        ascii_generator = ASCIIGenerator(text, font, custom_char)
        ascii_art = ascii_generator.scale_art(width, height)
        colored_art = self.color_handler.color_text(ascii_art, color)

        return ascii_art, colored_art

    def save_art(self, ascii_art, filename):
        self.file_manager.save_to_file(ascii_art, filename + ".txt")

    def set_dimensions(self, prompt: str, default: int = 1) -> int:
        while True:
            user_input = input(f"{prompt} (1-10, стандартно {default}): ")
            if user_input.isdigit() and 1 <= int(user_input) <= 10:
                return int(user_input)
            elif user_input == "":
                return default
            else:
                print("Неправильний ввід. Введіть ціле число від 1 до 10.")