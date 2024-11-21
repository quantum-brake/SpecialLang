from Shared.Classes.memory import Memory


class InputHandler:
    def __init__(self):
        self.memory = Memory()

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
