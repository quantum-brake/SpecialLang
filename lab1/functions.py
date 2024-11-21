import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


import math
from variables import decimals, memory, history_file

history_file = os.path.join(os.path.dirname(__file__), history_file)

def set_decimals(value):
    global decimals
    decimals = value

def get_decimals():
    return decimals

def set_memory(value):
    global memory
    memory = value

def get_memory():
    return memory

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
    except FileNotFoundError as e:
        raise FileNotFoundError("Історія обчислень відсутня.")

def change_settings():
    new_decimals = input(f"Поточна кількість десяткових знаків: {get_decimals()}. Введіть нову кількість: ")
    if new_decimals.isalpha():
        raise TypeError("Помилка! Введіть ціле (додатнє) число для кількості десяткових знаків.")
    elif int(new_decimals) < 0:
        raise ValueError("Помилка! Введіть ціле (додатнє) число для кількості десяткових знаків.")
    set_decimals(int(new_decimals))
    print(f"Кількість десяткових знаків змінено на {new_decimals}.")
        

def store_memory_value():
    try:
        custom_value = float(input("Введіть число для збереження в пам'ять: "))
        set_memory(custom_value)
        print(f"Число {custom_value} збережене в пам'ять (M).")
    except ValueError as e:
        raise ValueError("Помилка! Введіть дійсне число.")


def get_input():
    num1_input = input("Введіть перше число (або 'm' для використання збереженого значення): ")

    if num1_input.lower() == 'm':
        num1 = get_memory() 
    elif num1_input.isalpha():
        raise TypeError("Необхідно ввести число")
    elif num1_input.isnumeric():
        num1 = float(num1_input)
    else:
        raise ValueError("Необхідно ввести число")

    operator = get_operator()  
    
    if operator != '√':
        while True:
                num2_input = input("Введіть друге число (або 'm' для використання збереженого значення): ")
                if num2_input.lower() == 'm':
                    num2 = get_memory() 
                elif num1_input.isalpha():
                    raise TypeError("Необхідно ввести число")
                elif num2_input.isnumeric():
                    num2 = float(num2_input)
                else:
                    raise ValueError("Необхідно ввести число")
                break  
    else:
        num2 = None
    return num1, operator, num2
    
    

def calculate(num1, operator, num2):
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

def calculator(history_file):
    num1, operator, num2 = get_input()
    result = calculate(num1, operator, num2)
    result = round(result, get_decimals())
    print(f"Результат: {result}")

    save_to_history(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}", history_file)

    save_to_memory = input("Бажаєте зберегти результат у пам'ять? (Y/N): ").lower()
    if save_to_memory == 'y':
        set_memory(result)
        print(f"Результат {result} збережений у пам'ять (M).")
    
    try_again = input("Бажаєте повторити обчислення? (Y/N): ").lower()
    if try_again == 'y':
        calculator(history_file)

def main():
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
                calculator(history_file)
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)

        elif choice == '2':
            try:
                display_history(history_file)
            except FileNotFoundError as e:
                print(e)

        elif choice == '3':
            try:
                store_memory_value()
            except ValueError as e:
                print(e)

        elif choice == '4':
            print(f"число збережене у пам'яті: {get_memory()}")

        elif choice == '5':
            try:
                change_settings()
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)

        elif choice == '6':
            print("Вихід з калькулятора.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")