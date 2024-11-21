from tabulate import tabulate
from Classes.data_repository import DataRepository
from Classes.api_client import APIClient
from Classes.file_manager import FileManager
from Classes.User_input_handler import UserInputHandler


class ConsoleApp:
    def __init__(self):
        self.api_client = APIClient("https://jsonplaceholder.typicode.com")
        self.repo = DataRepository(self.api_client)
        self.file_manager = FileManager()
        self.user_input_handler = UserInputHandler(self.repo)
        self.history = self.file_manager.load_history()

    def view_data(self):
        data_type = self.user_input_handler.select_data_type()
        if data_type:
            view_type = input("Введіть формат відображення (table/list): ").strip().lower()
            data = self.repo.fetch_data(data_type)
            self.display_data(data, view_type)
            self.add_to_history(f"Отримати {data_type}", data)

    def display_data(self, data, view_type="table"):
        headers = data[0].keys() if data else []
        table = [item.values() for item in data]

        if view_type == "table":
            print(tabulate(table, headers=headers, tablefmt="grid"))
        elif view_type == "list":
            for item in data:
                print(item)
        else:
            print("Невірний вибір формату.")

    def add_data(self):
        data_type = self.user_input_handler.select_data_type()
        if data_type:
            data = self.user_input_handler.create_data(data_type)
            if data:
                added_data = self.repo.add_data(data_type, data)
                print(f"Дані додано: {added_data}")
                self.file_manager.save_history(self.history)
                self.add_to_history(f"Додати {data_type}", data)
            else:
                print("Не вдалося створити дані.")

    def delete_data(self):
        result = self.user_input_handler.delete_data()
        if result:
            data_type, record_id = result
            self.add_to_history(f"Видалити {data_type}", f"id={record_id}")
        else:
            print("Не вдалося видалити дані. Спробуйте ще раз.")

    def save_to_file(self):
        data_type = self.user_input_handler.select_data_type()
        data = self.repo.fetch_data(data_type)
        file_format = input("Оберіть формат збереження (txt, json, csv): ").strip().lower()
        self.file_manager.save_data_to_file(data, data_type, file_format)

    def view_history(self):
        self.history = self.file_manager.load_history()
        self.file_manager.view_history(self.history)

    def add_to_history(self, query, result):
        self.history.append((query, result))
        self.file_manager.save_history(self.history)
