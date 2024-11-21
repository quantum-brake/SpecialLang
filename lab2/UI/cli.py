import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


from Shared.Classes.Calculator import Calculator


def user_input_interface():
    calc = Calculator()

    while True:
        print("\nМеню:")
        print("1. Провести обчислення")
        print("2. Вивести історію обчислень")
        print("3. Записати число у памʼять")
        print("4. Вивести число з памʼяті")
        print("5. Поміняти налаштування (кількість десяткових знаків)")
        print("6. Вийти з калькулятора")

        choice = input("Оберіть опцію (1-6): ")

        if choice == '1':
            try:
                calc.calculator()
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)

        elif choice == '2':
            try:
                calc.history_manager.display_history()
            except FileNotFoundError as e:
                print(e)

        elif choice == '3':
            try:
                custom_value = float(input("Введіть число для збереження в пам'ять: "))
                calc.input_handler.memory.set_memory(custom_value)
                print(f"Число {custom_value} збережене в пам'ять (M).")
            except ValueError as e:
                print(e)

        elif choice == '4':
            print(f"Число збережене у пам'яті: {calc.input_handler.memory.get_memory()}")

        elif choice == '5':
            try:
                calc.settings.change_settings()
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)

        elif choice == '6':
            print("Вихід з калькулятора.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
