import math
from abc import ABC, abstractmethod
from variables import decimals, memory, history_file


class Memory:
    def __init__(self):
        self.__memory = memory

    def set_memory(self, value):
        self.__memory = value

    def get_memory(self):
        return self.__memory


class CalculatorSettings:
    def __init__(self):
        self.__decimals = decimals

    def set_decimals(self, value):
        self.__decimals = value

    def get_decimals(self):
        return self.__decimals

    def change_settings(self):
        new_decimals = input(f"Поточна кількість десяткових знаків: {self.get_decimals()}. Введіть нову кількість: ")
        if new_decimals.isalpha():
            raise TypeError("Введена літера! Введіть ціле (додатнє) число для кількості десяткових знаків.")
        if int(new_decimals) < 0:
            raise ValueError("Введено число менше 0! Введіть ціле (додатнє) число для кількості десяткових знаків.")
        self.set_decimals(int(new_decimals))
        print(f"Кількість десяткових знаків змінено на {new_decimals}.")

class HistoryManager:
    def __init__(self):
        self.__history_file = history_file

    def save_to_history(self, entry):
        with open(self.__history_file, "a") as file:
            file.write(entry + "\n")

    def display_history(self):
        try:
            with open(self.__history_file, "r") as file:
                history = file.readlines()
            if not history:
                print("Історія обчислень пуста.")
            else:
                print("Історія обчислень:")
                for entry in history:
                    print(entry.strip())
        except FileNotFoundError as e:
            raise FileNotFoundError("Історія обчислень відсутня.")



class CalculatorInput(ABC):
    def __init__(self):
        self.memory = Memory()
        self.settings = CalculatorSettings()
        self.history_manager = HistoryManager()

    def check_operator(self, operator):
        return operator in ['+', '-', '*', '/', '^', '√', '%']

    def get_operator(self):
        while True:
            operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            if self.check_operator(operator):
                return operator
            else:
                print("Невірний оператор. Будь ласка, введіть правильний оператор.")

    def get_input(self):
        num1_input = input("Введіть перше число (або 'm' для використання збереженого значення): ")
        if num1_input.lower() == 'm':
            num1 = self.memory.get_memory()
        elif num1_input.isalpha():
            raise TypeError("Необхідно ввести число")
        elif num1_input.isnumeric():
            num1 = float(num1_input)
        else:
            raise ValueError("Необхідно ввести число")

        operator = self.get_operator()
        if operator != '√':
            while True:
                num2_input = input("Введіть друге число (або 'm' для використання збереженого значення): ")
                if num2_input.lower() == 'm':
                    num2 = self.memory.get_memory()
                elif num2_input.isalpha():
                    raise TypeError("Необхідно ввести число")
                elif num2_input.isnumeric():
                    num2 = float(num2_input)
                else:
                    raise ValueError("Необхідно ввести число")
                break
        else:
            num2 = None
        return num1, operator, num2
    
    @abstractmethod
    def calculate(self):
        pass


class Calculator(CalculatorInput):
    def perform_operation(self, num1, operator, num2):
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                if num2 == 0:
                    raise ZeroDivisionError("Ділення на нуль неможливе")
                return num1 / num2
            case "^":
                return num1 ** num2
            case "√":
                if num1 < 0:
                    raise ValueError("Квадратний корінь з від'ємного числа неможливий")
                return math.sqrt(num1)
            case "%":
                if num2 == 0:
                    raise ZeroDivisionError("Неможливо отримати залишок з нуля")
                return num1 % num2
            case _:
                raise ValueError("Недійсний оператор!")

    def calculate(self):
        num1, operator, num2 = self.get_input()
        result = self.perform_operation(num1, operator, num2)
        result = round(result, self.settings.get_decimals())
        print(f"Результат: {result}")

        self.history_manager.save_to_history(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}")
        
        save_to_memory = input("Бажаєте зберегти результат у пам'ять? (Y/N): ").lower()
        if save_to_memory == 'y':
            self.memory.set_memory(result)
            print(f"Результат {result} збережений у пам'ять (M).")
