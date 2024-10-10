from classes import Calculator

def main():
    try:
        calc = Calculator()
    except TypeError as e:
        print(e)
        exit(1)

    while True:
        print("\nМеню:")
        print("1. Провести обчислення")
        print("2. Вивести історію обчислень")
        print("3. Записати число у памʼять")
        print("4. Вивести число з памʼяті")
        print("5. Поміняти налаштування (кількість десяткових знаків)")
        print("6. Вийти з калькулятора")

        choice = input("Оберіть опцію (1-6): ")
        match choice:
            case "1":
                try:
                    calc.calculate()
                except (ValueError, TypeError, ZeroDivisionError) as e:
                    print(e)
            case "2":
                try:
                    calc.history_manager.display_history()
                except FileNotFoundError as e:
                    print(e)
            case "3":
                try:
                    custom_value = float(input("Введіть число для збереження в пам'ять: "))
                    calc.memory.set_memory(custom_value)
                    print(f"Число {custom_value} збережене в пам'ять (M).")
                except ValueError as e:
                    print(e)
            case "4":
                print(f"Число збережене у пам'яті: {calc.memory.get_memory()}")
            case "5":
                try:
                    calc.settings.change_settings()
                except (ValueError, TypeError) as e:
                    print(e)
            case "6":
                print("Вихід з калькулятора.")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")
