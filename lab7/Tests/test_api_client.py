import unittest

import requests

from Classes.api_client import APIClient
from unittest.mock import patch

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = APIClient("https://jsonplaceholder.typicode.com")

    @patch("requests.get")
    def test_get_data_success(self, mock_get):
        mock_get.return_value.json.return_value = [{"id": 1, "title": "Test Post"}]
        mock_get.return_value.status_code = 200
        result = self.client.get_data("posts")
        self.assertEqual(result, [{"id": 1, "title": "Test Post"}])

    @patch("requests.get")
    def test_get_data_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException("API error")
        result = self.client.get_data("posts")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
