import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from Classes.service import Service

def user_interface():
    service = Service()

    while True:
        print("\n=== Меню ===")
        print("1. Вибрати файл")
        print("2. Обрати тип візуалізації")
        print("3. Відобразити дані")
        print("4. Зберегти графік у файл")
        print("5. Вийти")

        choice = input("Оберіть пункт меню (1-5): ").strip()

        match choice:
            case '1':
                service.select_file()
            case '2':
                service.select_visualization()
            case '3':
                service.display_data()
            case '4':
                service.save_to_file()
            case '5':
                print("Вихід із програми. До побачення!")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")

