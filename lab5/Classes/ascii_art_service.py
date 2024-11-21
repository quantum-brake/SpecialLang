from Classes.FileManager import FileManager
from Classes.ascii_art_displayer import ArtDisplayer
from Classes.user_input_handler import UserInputManager


class AsciiArtService:
    def __init__(self):
        self.file_manager = FileManager()
        self.art_displayer = ArtDisplayer()
        self.user_input_manager = UserInputManager()
        self.ascii_generator = self.user_input_manager.ascii_art_generator

    def update_shape(self):
        return self.user_input_manager.update_shape()

    def update_size(self):
        return self.user_input_manager.update_size()

    def update_color(self):
        self.art_displayer.colorizer.list_colors()
        self.art_displayer.colorizer.update_color()

    def display_ascii_art(self):
        self.ascii_generator.set_shape(self.ascii_generator.get_shape_type(), self.ascii_generator.get_size())
        self.ascii_generator.rotate_shape(self.ascii_generator.get_x(), self.ascii_generator.get_y(),
                                          self.ascii_generator.get_z())
        return self.art_displayer.display_ascii_art(self.ascii_generator.get_shape(),
                                                    self.art_displayer.colorizer.get_color())

    def save_to_file(self):
        filename = input("Введіть назву файла у який зберегти ASCII art (наприклад, art.txt): ")
        self.file_manager.save_to_file(self.ascii_generator.get_shape().project_to_2d(), filename)

    def update_x(self):
        return self.user_input_manager.update_x()

    def update_y(self):
        return self.user_input_manager.update_y()

    def update_z(self):
        return self.user_input_manager.update_z()
