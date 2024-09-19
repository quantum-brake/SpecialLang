import math
from variables import set_memory, get_memory
from appsettings import get_decimals, set_decimals


def check_operator(operator):
    return operator in ['+', '-', '*', '/', '^', '√', '%']

def get_operator():
    while True:
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if check_operator(operator):
            return operator
        else:
            print("Невірний оператор. Будь ласка, введіть правильний оператор.")

def save_to_history(entry, history_file):
    with open(history_file, "a") as file:
        file.write(entry + "\n")

def display_history(history_file):
    try:
        with open(history_file, "r") as file:
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
        if new_decimals < 0:
            print("Неможливо використати відʼємне значення.")
            change_settings()
        set_decimals(new_decimals)
        print(f"Кількість десяткових знаків змінено на {new_decimals}.")
    except ValueError:
        print("Помилка! Введіть ціле (додатнє) число для кількості десяткових знаків.")

def store_memory_value():
    try:
        custom_value = float(input("Введіть число для збереження в пам'ять: "))
        set_memory(custom_value)
        print(f"Число {custom_value} збережене в пам'ять (M).")
    except ValueError:
        print("Помилка! Введіть дійсне число.")

def get_input():
    try:
        num1_input = input("Введіть перше число (або 'm' для використання збереженого значення): ")
        num1 = get_memory() if num1_input.lower() == 'm' else float(num1_input)

        operator = get_operator()  
        
        if operator != '√':
            while True:
                try:
                    num2_input = input("Введіть друге число (або 'm' для використання збереженого значення): ")
                    num2 = get_memory() if num2_input.lower() == 'm' else float(num2_input)
                    break  
                except ValueError:
                    print("Неправильне введення другого числа. Спробуйте ще раз.")
        else:
            num2 = None

        return num1, operator, num2
    except ValueError:
        return get_input()

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

def calculator(history_file):
    while True:
        num1, operator, num2 = get_input()
        try:
            result = calculate(num1, operator, num2)
            result = round(result, get_decimals())
            print(f"Результат: {result}")

            save_to_history(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}", history_file)

            save_to_memory = input("Бажаєте зберегти результат у пам'ять? (Y/N): ").lower()
            if save_to_memory == 'y':
                set_memory(result)
                print(f"Результат {result} збережений у пам'ять (M).")
            
            try_again = input("Бажаєте повторити обчислення? (Y/N): ").lower()
            if try_again == 'n':
                break
        
        except Exception as e:
            print(f"Помилка: {e}")