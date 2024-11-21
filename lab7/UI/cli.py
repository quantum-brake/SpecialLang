import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from Classes.console_app import ConsoleApp


def user_interface():
    console_app = ConsoleApp()

    while True:
        print("\nМеню:")
        print("1. Перегляд даних")
        print("2. Додати дані")
        print("3. Видалити дані")
        print("4. Зберегти у файл")
        print("5. Перегляд історії")
        print("6. Вихід")

        choice = input("Виберіть опцію: ").strip()

        match choice:
            case '1':
                console_app.view_data()
            case '2':
                console_app.add_data()
            case '3':
                console_app.delete_data()
            case '4':
                console_app.save_to_file()
            case '5':
                console_app.view_history()
            case '6':
                print("Вихід з програми...")
                break
            case _:
                print("Неправильний вибір. Спробуйте ще раз.")

