import json
import csv
import os


class FileManager:
    def __init__(self, data_directory="Data/"):
        self._data_directory = data_directory
        self._history_file = "history.json"

    def load_history(self):
        file_path = os.path.join(self._data_directory, self._history_file)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                return json.load(f)
        return []

    def save_history(self, history):
        file_path = os.path.join(self._data_directory, self._history_file)
        with open(file_path, "w") as f:
            json.dump(history, f, indent=4)

    def view_history(self, history):
        if not history:
            print("Історія порожня.")
            return
        print("\nІсторія запитів:")
        for idx, (query, result) in enumerate(history, start=1):
            print(f"{idx}. Запит: {query}")
            print("   Результат:", result)
            print("-" * 40)

    def save_data_to_file(self, data, data_type, file_format):
        file_path = os.path.join(self._data_directory, data_type)
        if not data:
            print(f"Немає даних для {data_type}.")
            return

        if file_format == "txt":
            with open(f"{file_path}.txt", "w") as f:
                for item in data:
                    f.write(f"{item}\n\n")
            print(f"Дані для {data_type} збережені у файл {data_type}.txt")

        elif file_format == "json":
            with open(f"{file_path}.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Дані для {data_type} збережені у файл {data_type}.json")

        elif file_format == "csv":
            with open(f"{file_path}.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(data[0].keys())  # Заголовки
                for item in data:
                    writer.writerow(item.values())
            print(f"Дані для {data_type} збережені у файл {data_type}.csv")

        else:
            print("Невірний формат файлу.")
