import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import os
from Classes.file_manager import FileManager


class TestFileManager(unittest.TestCase):

    def setUp(self):
        # Ініціалізація об'єкт з тестовою директорією
        self.data_directory = "./test_data/"
        self.file_manager = FileManager(self.data_directory)
        self.history_file = os.path.join(self.data_directory, "history.json")
        self.history = [{"query": "Test Query", "result": "Test Result"}]

    @patch("builtins.open", new_callable=mock_open,
           read_data=json.dumps([{"query": "Test Query", "result": "Test Result"}]))
    @patch("os.path.exists", return_value=True)
    def test_load_history(self, mock_exists, mock_open_file):
        history = self.file_manager.load_history()
        self.assertEqual(history, self.history)
        mock_open_file.assert_called_once_with(self.history_file, "r")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_history(self, mock_open_file):
        self.file_manager.save_history(self.history)
        mock_open_file.assert_called_once_with(self.history_file, "w")
        # mock_open_file().write.assert_called_once_with(json.dumps(self.history, indent=4))

    @patch("builtins.print")
    def test_view_history_empty(self, mock_print):
        self.file_manager.view_history([])
        mock_print.assert_called_once_with("Історія порожня.")


    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_save_data_to_txt(self, mock_print, mock_open_file):
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        self.file_manager.save_data_to_file(data, "users", "txt")
        mock_open_file.assert_called_once_with(os.path.join(self.data_directory, "users.txt"), "w")
        mock_print.assert_called_once_with("Дані для users збережені у файл users.txt")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_save_data_to_json(self, mock_print, mock_open_file):
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        self.file_manager.save_data_to_file(data, "users", "json")
        mock_open_file.assert_called_once_with(os.path.join(self.data_directory, "users.json"), "w")
        # mock_open_file().write.assert_called_once_with(json.dumps(data, indent=4))
        mock_print.assert_called_once_with("Дані для users збережені у файл users.json")

    @patch("builtins.open", new_callable=mock_open)
    @patch("csv.writer")
    @patch("builtins.print")
    def test_save_data_to_csv(self, mock_print, mock_csv_writer, mock_open_file):
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        mock_writer_instance = MagicMock()
        mock_csv_writer.return_value = mock_writer_instance
        self.file_manager.save_data_to_file(data, "users", "csv")


    @patch("builtins.print")
    def test_save_data_to_file_invalid_format(self, mock_print):
        data = [{"name": "Alice", "age": 30}]
        self.file_manager.save_data_to_file(data, "users", "xml")
        mock_print.assert_called_once_with("Невірний формат файлу.")

    @patch("builtins.print")
    def test_save_data_to_file_no_data(self, mock_print):
        self.file_manager.save_data_to_file([], "users", "json")
        mock_print.assert_called_once_with("Немає даних для users.")


if __name__ == "__main__":
    unittest.main()
