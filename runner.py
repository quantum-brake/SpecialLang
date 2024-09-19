from functions import calculator, display_history, store_memory_value, change_settings
from variables import history_file

def main():
    while True:
        print("\nМеню:")
        print("1. Провести обчислення")
        print("2. Вивести історію обчислень")
        print("3. Записати власне число в пам'ять")
        print("4. Поміняти налаштування (кількість десяткових знаків)")
        print("5. Вийти з калькулятора")

        choice = input("Оберіть опцію (1-5): ")

        if choice == '1':
            calculator(history_file)

        elif choice == '2':
            display_history(history_file)

        elif choice == '3':
            store_memory_value()

        elif choice == '4':
            change_settings()

        elif choice == '5':
            print("Вихід з калькулятора.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
