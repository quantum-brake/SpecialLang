from Shared.Variables.calculator_variables import history_file
import os


class HistoryManager:
    def __init__(self):
        self._history_file = history_file
        self._data_directory = "Data/"
        self._history_file_path = os.path.join(self._data_directory, self._history_file)

    def save_to_history(self, entry):
        with open(self._history_file_path, "a") as file:
            file.write(entry + "\n")

    def display_history(self):
        try:
            with open(self._history_file_path, "r") as file:
                history = file.readlines()
            if not history:
                print("Історія обчислень пуста.")
            else:
                print("Історія обчислень:")
                for entry in history:
                    print(entry.strip())
        except FileNotFoundError as e:
            raise FileNotFoundError("Історія обчислень відсутня.")