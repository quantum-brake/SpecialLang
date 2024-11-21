from Shared.Classes.calculatorSettings import CalculatorSettings
from Shared.Classes.inputHandler import InputHandler
from Shared.Classes.historyManager import HistoryManager
import math

class Calculator:
    def __init__(self):
        self.settings = CalculatorSettings()
        self.input_handler = InputHandler()
        self.history_manager = HistoryManager()

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

    def calculator(self):
        num1, operator, num2 = self.input_handler.get_input()
        result = self.perform_operation(num1, operator, num2)
        result = round(result, self.settings.get_decimals())
        print(f"Результат: {result}")
        self.history_manager.save_to_history(f"{num1} {operator} {num2 if num2 is not None else ''} = {result}")
        save_to_memory = input("Бажаєте зберегти результат у пам'ять? (Y/N): ").lower()
        if save_to_memory == 'y':
            self.input_handler.memory.set_memory(result)
            print(f"Результат {result} збережений у пам'ять (M).")
