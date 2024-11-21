import unittest
from Classes.data_repository import DataRepository
from unittest.mock import MagicMock

class TestDataRepository(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.repo = DataRepository(self.mock_client)

    def test_initialize_id_counters(self):
        self.mock_client.get_data.return_value = [{"id": 1}]
        counters = self.repo.initialize_id_counters()
        self.assertEqual(counters["posts"], 2)

    def test_add_data(self):
        data = {"title": "New Post"}
        result = self.repo.add_data("posts", data)
        self.assertEqual(result["id"], 1)
        self.assertIn(result, self.repo.local_data["posts"])

    def test_delete_data_nonexistent_id(self):
        self.repo.local_data["posts"] = [{"id": 1, "title": "Test Post"}]
        result = self.repo.delete_data("posts", 999)  # Non-existent ID
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
