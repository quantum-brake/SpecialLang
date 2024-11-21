import unittest
from unittest.mock import MagicMock, patch
from Classes.data_types import DataTypes


class TestDataTypes(unittest.TestCase):

    def setUp(self):
        # Create a mock for the repository (repo)
        self.repo = MagicMock()
        # Set up the DataFactory instance
        self.data_factory = DataTypes(self.repo)

    @patch('builtins.input', side_effect=["1", "Test Post", "This is a test post"])
    def test_create_post_data(self, mock_input):
        # Mock the repo's id_counters for posts
        self.repo.id_counters = {"posts": 1}

        # Call the method under test
        post_data = self.data_factory.create_post_data()

        # Assert that the returned post data matches the expected structure
        expected_post_data = {
            "userID": 1,
            "id": 1,
            "title": "Test Post",
            "body": "This is a test post"
        }
        self.assertEqual(post_data, expected_post_data)
        # Ensure the correct input calls were made
        mock_input.assert_any_call("Введіть userID: ")
        mock_input.assert_any_call("Введіть заголовок поста: ")
        mock_input.assert_any_call("Введіть текст поста: ")

    @patch('builtins.input', side_effect=["1", "Test Commenter", "test@example.com", "This is a test comment"])
    def test_create_comment_data(self, mock_input):
        # Mock the repo's id_counters for comments
        self.repo.id_counters = {"comments": 1}

        # Call the method under test
        comment_data = self.data_factory.create_comment_data()

        # Assert that the returned comment data matches the expected structure
        expected_comment_data = {
            "postID": 1,
            "id": 1,
            "name": "Test Commenter",
            "email": "test@example.com",
            "body": "This is a test comment"
        }
        self.assertEqual(comment_data, expected_comment_data)
        # Ensure the correct input calls were made
        mock_input.assert_any_call("Введіть postID: ")
        mock_input.assert_any_call("Введіть ім'я коментатора: ")
        mock_input.assert_any_call("Введіть email коментатора: ")
        mock_input.assert_any_call("Введіть текст коментаря: ")

    @patch('builtins.input', side_effect=["1", "Test Todo", "True"])
    def test_create_todo_data(self, mock_input):
        # Mock the repo's id_counters for todos
        self.repo.id_counters = {"todos": 1}

        # Call the method under test
        todo_data = self.data_factory.create_todo_data()

        # Assert that the returned todo data matches the expected structure
        expected_todo_data = {
            "userID": 1,
            "id": 1,
            "title": "Test Todo",
            "completed": True
        }
        self.assertEqual(todo_data, expected_todo_data)
        # Ensure the correct input calls were made
        mock_input.assert_any_call("Введіть userID: ")
        mock_input.assert_any_call("Введіть заголовок задачі: ")
        mock_input.assert_any_call("Чи виконана задача (True/False): ")

    @patch('builtins.input',
           side_effect=["John Doe", "johndoe", "john@example.com", "123 Main St", "555-5555", "johndoe.com",
                        "Example Inc."])
    def test_create_user_data(self, mock_input):
        # Mock the repo's id_counters for users
        self.repo.id_counters = {"users": 1}

        # Call the method under test
        user_data = self.data_factory.create_user_data()

        # Assert that the returned user data matches the expected structure
        expected_user_data = {
            "id": 1,
            "name": "John Doe",
            "username": "johndoe",
            "email": "john@example.com",
            "address": "123 Main St",
            "phone": "555-5555",
            "website": "johndoe.com",
            "company": "Example Inc."
        }
        self.assertEqual(user_data, expected_user_data)
        # Ensure the correct input calls were made
        mock_input.assert_any_call("Введіть ім'я користувача: ")
        mock_input.assert_any_call("Введіть username: ")
        mock_input.assert_any_call("Введіть email: ")
        mock_input.assert_any_call("Введіть адресу: ")
        mock_input.assert_any_call("Введіть номер телефону: ")
        mock_input.assert_any_call("Введіть вебсайт: ")
        mock_input.assert_any_call("Введіть компанію: ")

    def test_create_data_invalid_type(self):
        # Test the behavior of create_data for an invalid data type
        data = self.data_factory.create_data("invalid_data_type")
        self.assertIsNone(data)


if __name__ == "__main__":
    unittest.main()
