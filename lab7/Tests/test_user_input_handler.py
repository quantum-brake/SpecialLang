import unittest
from unittest.mock import patch, MagicMock
from Classes.user_input_handler import UserInputHandler

class TestUserInputHandler(unittest.TestCase):

    def setUp(self):
        # Ініалізація моків та значень для тестів
        self.repo = MagicMock()
        self.repo.id_counters = {
            "posts": 1,
            "comments": 1,
            "todos": 1,
            "users": 1
        }
        self.handler = UserInputHandler(self.repo)

    def test_select_data_type_valid(self):
        with patch('builtins.input', return_value='posts'):
            data_type = self.handler.select_data_type()
            self.assertEqual(data_type, "posts")

    def test_select_data_type_invalid(self):
        with patch('builtins.input', return_value='invalid_type'), patch('builtins.print') as mock_print:
            data_type = self.handler.select_data_type()
            self.assertIsNone(data_type)
            mock_print.assert_called_with("Невірний вибір типу даних.")

    def test_add_post_data(self):
        with patch('builtins.input', side_effect=["1", "Test Title", "Test Body"]):
            data = self.handler.add_post_data()
            self.assertEqual(data, {"userID": 1, "id": 1, "title": "Test Title", "body": "Test Body"})

    def test_add_comment_data(self):
        with patch('builtins.input', side_effect=["1", "Commenter", "test@example.com", "Test Comment"]):
            data = self.handler.add_comment_data()
            self.assertEqual(data, {"postID": 1, "id": 1, "name": "Commenter", "email": "test@example.com", "body": "Test Comment"})

    def test_add_todo_data_completed_true(self):
        with patch('builtins.input', side_effect=["1", "Test Todo", "True"]):
            data = self.handler.add_todo_data()
            self.assertEqual(data, {"userID": 1, "id": 1, "title": "Test Todo", "completed": True})

    def test_add_todo_data_completed_false(self):
        with patch('builtins.input', side_effect=["1", "Test Todo", "False"]):
            data = self.handler.add_todo_data()
            self.assertEqual(data, {"userID": 1, "id": 1, "title": "Test Todo", "completed": False})


    def test_delete_data_valid(self):
        with patch('builtins.input', side_effect=["posts", "1"]), patch('builtins.print'):
            data_type, record_id = self.handler.delete_data()
            self.assertEqual(data_type, "posts")
            self.assertEqual(record_id, 1)
            self.repo.delete_data.assert_called_once_with("posts", 1)



if __name__ == '__main__':
    unittest.main()
