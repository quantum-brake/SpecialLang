import unittest
from unittest.mock import patch, MagicMock
from Classes.console_app import ConsoleApp


class TestConsoleApp(unittest.TestCase):

    def setUp(self):
        # Створюються моки та ініціалізується об'єкт для кожного тесту
        self.app = ConsoleApp()
        self.app.repo = MagicMock()
        self.app.file_manager = MagicMock()
        self.app.user_input_handler = MagicMock()

    def test_view_data_with_table_format(self):
        self.app.repo.fetch_data.return_value = [{"id": 1, "name": "Test"}]
        self.app.user_input_handler.select_data_type.return_value = "test_data"

        with patch('builtins.input', return_value='table'), patch('builtins.print') as mock_print:
            self.app.view_data()

            self.app.repo.fetch_data.assert_called_once_with("test_data")
            mock_print.assert_called()  # Перевірка, що `print` був викликаний.

    def test_view_data_with_list_format(self):
        self.app.repo.fetch_data.return_value = [{"id": 1, "name": "Test"}]
        self.app.user_input_handler.select_data_type.return_value = "test_data"

        with patch('builtins.input', return_value='list'), patch('builtins.print') as mock_print:
            self.app.view_data()

            self.app.repo.fetch_data.assert_called_once_with("test_data")
            mock_print.assert_called_with({'id': 1, 'name': 'Test'})

    def test_view_data_invalid_format(self):
        self.app.repo.fetch_data.return_value = [{"id": 1, "name": "Test"}]
        self.app.user_input_handler.select_data_type.return_value = "test_data"

        with patch('builtins.input', return_value='invalid_format'), patch('builtins.print') as mock_print:
            self.app.view_data()

            mock_print.assert_any_call("Невірний вибір формату.")


    def test_delete_data_success(self):
        self.app.user_input_handler.delete_data.return_value = ("posts", 1)
        self.app.repo.delete_data.return_value = True

        self.app.delete_data()

    def test_save_to_file(self):
        self.app.user_input_handler.select_data_type.return_value = "posts"
        self.app.repo.fetch_data.return_value = [{"id": 1, "title": "Test Post"}]

        with patch('builtins.input', return_value='json'):
            self.app.save_to_file()

            self.app.file_manager.save_data_to_file.assert_called_once_with([{"id": 1, "title": "Test Post"}], "posts",
                                                                            "json")

    def test_view_history(self):
        self.app.file_manager.load_history.return_value = [("Запит", "Результат")]

        self.app.view_history()

        self.app.file_manager.view_history.assert_called_once_with([("Запит", "Результат")])

    def test_add_to_history(self):
        self.app.history = []
        self.app.add_to_history("Запит", "Результат")

        self.assertEqual(len(self.app.history), 1)
        self.app.file_manager.save_history.assert_called_once_with([("Запит", "Результат")])

    def test_display_data_table_format(self):
        data = [{"id": 1, "name": "Test"}]

        with patch('builtins.print') as mock_print:
            self.app.display_data(data, "table")

            mock_print.assert_called()  # Перевірка, що print був викликаний для таблиці

    def test_display_data_list_format(self):
        data = [{"id": 1, "name": "Test"}]

        with patch('builtins.print') as mock_print:
            self.app.display_data(data, "list")

            mock_print.assert_any_call({'id': 1, 'name': 'Test'})

    def test_display_data_invalid_format(self):
        data = [{"id": 1, "name": "Test"}]

        with patch('builtins.print') as mock_print:
            self.app.display_data(data, "invalid_format")

            mock_print.assert_any_call("Невірний вибір формату.")


if __name__ == '__main__':
    unittest.main()
