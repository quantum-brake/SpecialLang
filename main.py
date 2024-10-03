import math


memory = 0

def set_memory(value):
    global memory
    memory = value

def get_memory():
    return memory


DECIMALS = 2

def set_decimals(precision):
    global DECIMALS
    DECIMALS = precision

def get_decimals():
    return DECIMALS



def get_input():
    global memory
    try:
        num1_input = input("Введіть перше число (або 'm' для використання збереженого значення): ")
        num1 = get_memory() if num1_input.lower() == 'm' else float(num1_input)

        operator = get_operator()  # Виклик нової функції для перевірки оператора
        
        if operator != '√':
           while True:
                try:
                    num2_input = input("Введіть друге число (або 'm' для використання збереженого значення): ")
                    num2 = get_memory() if num2_input.lower() == 'm' else float(num2_input)
                    break  # Вихід з циклу, якщо ввід успішний
                except ValueError:
                    print("Неправильне введення другого числа. Спробуйте ще раз.")
        else:
            num2 = None

        return num1, operator, num2
    except ValueError:
        # print("Неправильне введення. Спробуйте ще раз.")
        return get_input()

def check_operator(operator):
    return operator in ['+', '-', '*', '/', '^', '√', '%']

def get_operator():
    while True:
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if check_operator(operator):
            return operator
        else:
            print("Невірний оператор. Будь ласка, введіть правильний оператор.")

def calculate(num1, operator, num2):
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе")
            return num1 / num2
        elif operator == "^":
            return num1 ** num2
        elif operator == "√":
            if num1 < 0:
                raise ValueError("Квадратний корінь з від'ємного числа неможливий")
            return math.sqrt(num1)
        elif operator == "%":
            if num2 == 0:
                raise ZeroDivisionError("Неможливо отримати залишок з нуля")
            return num1 % num2 
        else:
            raise ValueError("Недійсний оператор!")
    except Exception as e:
        raise

def calculator(history):
    while True:
        num1, operator, num2 = get_input()
        try:
            result = calculate(num1, operator, num2)
            result = round(result, get_decimals())  # Округлення результату
            print(f"Результат: {result}")
            history.append(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}")

            save_to_memory = input("Бажаєте зберегти результат у пам'ять? (Y/N): ").lower()
            if save_to_memory == 'y':
                set_memory(result)
                print(f"Результат {result} збережений у пам'ять (M).")
            
            try_again = input("Бажаєте повторити обчислення? (Y/N): ").lower()
            if try_again == 'n':
                break
        
        except Exception as e:
            print(f"Помилка: {e}")

# def display_history(history):
#     if not history:
#         print("Історія обчислень пуста.")
#     else:
#         print("Історія обчислень:")
#         for entry in history:
#             print(entry)

def save_to_history(entry, filename="history.txt"):
    with open(filename, "a") as file:
        file.write(entry + "\n")


def display_history(filename="history.txt"):
    try:
        with open(filename, "r") as file:
            history = file.readlines()
        if not history:
            print("Історія обчислень пуста.")
        else:
            print("Історія обчислень:")
            for entry in history:
                print(entry.strip())
    except FileNotFoundError:
        print("Історія обчислень відсутня.")


def change_settings():
    try:
        new_decimals = int(input(f"Поточна кількість десяткових знаків: {get_decimals()}. Введіть нову кількість: "))
        set_decimals(new_decimals)
        print(f"Кількість десяткових знаків змінено на {new_decimals}.")
    except ValueError:
        print("Помилка! Введіть ціле число для кількості десяткових знаків.")

def store_custom_value():
    try:
        custom_value = float(input("Введіть число для збереження в пам'ять: "))
        set_memory(custom_value)
        print(f"Число {custom_value} збережене в пам'ять (M).")
    except ValueError:
        print("Помилка! Введіть дійсне число.")



def main():
    # history = []
    history_file = "history.txt"

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
            store_custom_value()

        elif choice == '4':
            change_settings()

        elif choice == '5':
            print("Вихід з калькулятора.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
