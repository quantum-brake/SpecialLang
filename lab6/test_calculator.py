import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from unittest.mock import patch
from Shared.Classes.calculatorSettings import CalculatorSettings
from Shared.Classes.inputHandler import InputHandler
from Shared.Classes.historyManager import HistoryManager
from Shared.Classes.memory import Memory
from Shared.Classes.Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.perform_operation(5, '+', 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.perform_operation(5, '-', 3), 2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.perform_operation(5, '*', 3), 15)

    def test_division(self):
        self.assertEqual(self.calculator.perform_operation(6, '/', 3), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.perform_operation(6, '/', 0)

    def test_exponentiation(self):
        self.assertEqual(self.calculator.perform_operation(2, '^', 3), 8)

    def test_square_root(self):
        self.assertEqual(self.calculator.perform_operation(9, '√', None), 3)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.perform_operation(-9, '√', None)

    def test_modulo(self):
        self.assertEqual(self.calculator.perform_operation(10, '%', 3), 1)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.perform_operation(5, '&', 3)


class TestInputHandler(unittest.TestCase):
    def setUp(self):
        self.input_handler = InputHandler()

    @patch('builtins.input', side_effect=['+'])
    def test_get_operator_valid(self, mock_input):
        self.assertEqual(self.input_handler.get_operator(), '+')

    @patch('builtins.input', side_effect=['@', '+'])
    def test_get_operator_invalid_then_valid(self, mock_input):
        self.assertEqual(self.input_handler.get_operator(), '+')

    @patch('builtins.input', side_effect=['5', '+', '3'])
    def test_get_input(self, mock_input):
        with patch.object(self.input_handler.memory, 'get_memory', return_value=10):
            self.assertEqual(self.input_handler.get_input(), (5.0, '+', 3.0))

    def test_check_operator(self):
        self.assertTrue(self.input_handler.check_operator('+'))
        self.assertFalse(self.input_handler.check_operator('&'))


class TestHistoryManager(unittest.TestCase):
    def setUp(self):
        self.history_manager = HistoryManager()
        self.history_manager._history_file_path = 'Data/test_history.txt'  

    def tearDown(self):
        try:
            os.remove(self.history_manager._history_file_path)  
        except FileNotFoundError:
            pass

    def test_save_to_history(self):
        self.history_manager.save_to_history("5 + 3 = 8")
        with open(self.history_manager._history_file_path, 'r') as file:
            lines = file.readlines()
        self.assertEqual(lines[-1].strip(), "5 + 3 = 8")

    def test_display_history_empty(self):
        with self.assertRaises(FileNotFoundError):
            self.history_manager.display_history()


class TestCalculatorSettings(unittest.TestCase):
    def setUp(self):
        self.settings = CalculatorSettings()

    def test_get_decimals(self):
        self.settings.set_decimals(2)
        self.assertEqual(self.settings.get_decimals(), 2)

    @patch('builtins.input', side_effect=['2'])
    def test_change_settings_valid(self, mock_input):
        self.settings.change_settings()
        self.assertEqual(self.settings.get_decimals(), 2)

    @patch('builtins.input', side_effect=['-1'])
    def test_change_settings_invalid_negative(self, mock_input):
        with self.assertRaises(ValueError):
            self.settings.change_settings()

    @patch('builtins.input', side_effect=['abc'])
    def test_change_settings_invalid_non_numeric(self, mock_input):
        with self.assertRaises(TypeError):
            self.settings.change_settings()


class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_set_memory(self):
        self.memory.set_memory(10)
        self.assertEqual(self.memory.get_memory(), 10)

    def test_get_memory_default(self):
        self.assertEqual(self.memory.get_memory(), 0)  


if __name__ == '__main__':
    unittest.main()
