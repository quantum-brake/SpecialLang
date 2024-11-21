import os


class FileManager:
    def __init__(self, data_directory="Data/"):
        self._data_directory = data_directory

        if not os.path.exists(self._data_directory):
            os.makedirs(self._data_directory)

    def save_to_file(self, projection, filename):
        file_path = os.path.join(self._data_directory, filename)
        with open(file_path, 'w') as f:
            for row in projection:
                f.write("".join(row) + "\n")
        print(f"ASCII art збережено у {file_path}")

