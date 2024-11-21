import os


class FileManager:
    def __init__(self, data_directory="Data/"):
        self.data_directory = data_directory

        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

    def save_to_file(self, ascii_art, filename):
        file_path = os.path.join(self.data_directory, filename)
        with open(file_path, 'w', encoding="ascii") as f:
            f.write(ascii_art)
        print(f"ASCII art збережено у {file_path}")
