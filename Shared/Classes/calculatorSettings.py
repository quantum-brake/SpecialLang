from Shared.Variables.calculator_variables import decimals


class CalculatorSettings:
    def __init__(self):
        self.decimals = decimals

    def set_decimals(self, value):
        self.decimals = value

    def get_decimals(self):
        return self.decimals

    def change_settings(self):
        new_decimals = input(f"Поточна кількість десяткових знаків: {self.get_decimals()}. Введіть нову кількість: ")
        if new_decimals.isalpha():
            raise TypeError("Введена літера! Введіть ціле (додатнє) число для кількості десяткових знаків.")
        if int(new_decimals) < 0:
            raise ValueError("Введено число менше 0! Введіть ціле (додатнє) число для кількості десяткових знаків.")
        self.set_decimals(int(new_decimals))
        print(f"Кількість десяткових знаків змінено на {new_decimals}.")
