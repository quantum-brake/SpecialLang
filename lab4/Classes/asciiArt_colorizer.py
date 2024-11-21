import json
import os

class Colorizer:
    def __init__(self, config_path=os.path.join(os.path.dirname(__file__), "../Config/colors.json")):
        self._color = None
        with open(config_path, 'r') as config_file:
            self._config = json.load(config_file)
            self._colors = self._config["colors"]

    def colorize(self, text, color):
        if color in self._colors:
            return f"{self._colors[color]}{text}{self._colors['reset']}"
        return text

    def update_color(self):
        self._color = input("Enter color: ")

    def get_color(self):
        return self._color

    def list_colors(self, num_columns=4):
        color_names = [name for name in self._colors if name != "reset"]
        max_name_length = max(len(name) for name in color_names) + 2

        for i in range(0, len(color_names), num_columns):
            row = color_names[i:i + num_columns]
            formatted_row = [
                self.colorize(name.ljust(max_name_length), name) for name in row
            ]
            print("".join(formatted_row))