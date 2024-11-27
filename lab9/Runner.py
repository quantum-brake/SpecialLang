import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab1.functions import main as lab1
from lab2.UI.cli import user_input_interface as lab2
from lab3.UI.cli import user_input_interface as lab3
from lab4.UI.cli import user_input_interface as lab4
from lab5.UI.cli import user_input_interface as lab5
from lab6.run_test import main as lab6
from lab7.UI.cli import user_interface as lab7
from lab8.UI.cli import user_interface as lab8

class RunnerFacade:
    def __init__(self):
        self.labs = {
            1: self.run_lab1,
            2: self.run_lab2,
            3: self.run_lab3,
            4: self.run_lab4,
            5: self.run_lab5,
            6: self.run_lab6,
            7: self.run_lab7,
            8: self.run_lab8,
        }
    
    def show_menu(self):
        menu = (
            "\nМеню лабораторних робіт:\n"
            "1: Запустити лабораторну роботу 1\n"
            "2: Запустити лабораторну роботу 2\n"
            "3: Запустити лабораторну роботу 3\n"
            "4: Запустити лабораторну роботу 4\n"
            "5: Запустити лабораторну роботу 5\n"
            "6: Запустити лабораторну роботу 6 (тести)\n"
            "7: Запустити лабораторну роботу 7\n"
            "8: Запустити лабораторну роботу 8\n"
            "0: Вихід із програми\n"
        )
        print(menu)

    def run_lab(self, choice):
        if choice in self.labs:
            self.labs[choice]()
        elif choice == 0:
            print("Вихід із програми.")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def run_lab1(self):
        lab1()

    def run_lab2(self):
        lab2()

    def run_lab3(self):
        lab3()

    def run_lab4(self):
        lab4()

    def run_lab5(self):
        lab5()

    def run_lab6(self):
        lab6()

    def run_lab7(self):
        lab7()

    def run_lab8(self):
        lab8()

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("Оберіть лабораторну роботу: "))
                if choice == 0:
                    break
                self.run_lab(choice)
            except ValueError:
                print("Будь ласка, введіть коректний номер.")
